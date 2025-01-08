import base64
from base64 import b64decode, b64encode

import inflection
import xmltodict
from marshmallow import Schema, pre_load, post_dump, ValidationError, fields, validate
from marshmallow_dataclass import class_schema


class Base64Field(fields.Field):
    """
    base64 自定义属性
    """
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return base64.b64decode(value)
        except Exception as e:
            raise ValidationError(f"Error decoding Base64: {e}")

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        try:
            return base64.b64encode(value).decode('utf-8')
        except Exception as e:
            raise ValidationError(f"Error encoding Base64: {e}")


class XmlDataClassSchema(Schema):
    @pre_load
    def to_dict_pre(self, data, **kwargs):
        """将xml转换为dict"""
        xml = data["xml"]
        data_dict = xmltodict.parse(xml)[self.__model_name()]
        return data_dict

    @post_dump
    def to_xml_post(self, data, **kwargs):
        """将所有字段名从 snake_case 转换回 camelCase"""
        data_dict = {inflection.camelize(key, uppercase_first_letter=True):value for key, value in data.items()}
        # 将数据字典转换为 xml
        # result = xmltodict.unparse({self.__model_name(): data_dict}, full_document=False, pretty=True)
        result = xmltodict.unparse(data_dict, full_document=False, pretty=True)

        model_name = self.__model_name()
        root_xml = f"<{model_name}>{result}</{model_name}>"
        # 验证数据
        errors = self.validate({"xml": root_xml})
        if errors:
            raise ValidationError("Validation failed with the following errors: " + str(errors), data=errors)
        return result

    def __model_name(self):
        model_class = getattr(self.Meta, 'model', None)
        root = getattr(self.Meta, 'root', None)
        return model_class.__name__ if model_class else None

    @staticmethod
    def create(data_cls):
        # 自动生成基础 schema 并继承自 BaseSchema
        schema_cls = class_schema(data_cls, base_schema=XmlDataClassSchema)
        # 动态设置 Meta.model
        schema_cls.Meta.model = data_cls
        schema_cls.Meta.root = "xyz"

        return schema_cls()

    @staticmethod
    def to_xml(dataclass_instance):
        return XmlDataClassSchema.create(type(dataclass_instance)).dump(dataclass_instance)

    @staticmethod
    def from_xml(xml_data, dataclass_type):
        return XmlDataClassSchema.create(dataclass_type).load({"xml":xml_data})


if __name__ == '__main__':
    from dataclasses import dataclass, field
    from typing import Optional


    @dataclass
    class Person:
        person_id: int = field(metadata={"data_key":"PersonId"})
        first_name: str = field(metadata={"data_key":"FirstName", "validate":validate.Length(min=5, max=80)})
        last_name: str = field(metadata={"data_key":"LastName", "validate":validate.Length(min=5, max=80)})
        birth_date: Optional[str] = field(default=None, metadata={"data_key":"BirthDate"})
        photoImage: str = field(metadata={"data_key": "PhotoImage"}, default=None) # , "marshmallow_field": Base64Field()
        notes: Optional[str] = field(default=None, metadata={"data_key":"Notes"})


    @dataclass
    class Employee:
        employee_id: int = field(metadata={"data_key":"EmployeeId"})
        department: str = field(metadata={"data_key":"Department"})
        position: str = field(metadata={"data_key":"Position"})
        hire_date: Optional[str] = field(default=None, metadata={"data_key":"HireDate"})


    def test_xml_to_class():
        xml_data_person = """
        <Person>
            <PersonId>1</PersonId>
            <FirstName>Alice</FirstName>
            <LastName>Smith</LastName>
            <BirthDate>1990-01-01</BirthDate>
            <PhotoImage>cGhvdG8gZGF0YQ==</PhotoImage>
        </Person>
        """

        PersonSchema = XmlDataClassSchema.create(Person)
        try:
            person_instance = PersonSchema.load({"xml":xml_data_person})
            print(person_instance)  # 输出 Person (person_id=1, first_name='Alice', last_name='Smith', birth_date='1990-01-01')
        except ValidationError as e:
            print(e)

        xml_data_employee = """
        <Employee>
            <EmployeeId>2</EmployeeId>
            <Department>Sales</Department>
            <Position>Managerxxxxxxx</Position>
            <HireDate>2020-05-01</HireDate>
        </Employee>
        """

        EmployeeSchema = XmlDataClassSchema.create(Employee)
        employee_instance = EmployeeSchema.load({"xml":xml_data_employee})

        print(employee_instance)  # 输出 Employee(employee_id=2, department='Sales', position='Manager', hire_date='2020-05-01')

        print(XmlDataClassSchema.from_xml(xml_data_employee, Employee))


    def test_calss_to_xml():
        person_instance = Person(
            person_id=1,
            first_name="Alice",
            last_name="Smith",
            birth_date="1990-01-01",
            photoImage=b"photo data"
        )

        try:
            PersonSchema = XmlDataClassSchema.create(Person)
            data_dict = PersonSchema.dump(person_instance)
            print(data_dict)
        except ValidationError as e:
            print(e.data)

        # print(xml_output_person)
        # 输出 <?xml version='1.0' encoding='utf-8'?>
        #      <Person><personId>1</personId><firstName>Alice</firstName><lastName>Smith</lastName><birthDate>1990-01-01</birthDate></Person>

        employee_instance = Employee(
            employee_id=2,
            department="Sales",
            position="Manager",
            hire_date="2020-05-01"
        )

        EmployeeSchema = XmlDataClassSchema.create(Employee)
        data_dict = EmployeeSchema.dump(employee_instance)
        print(data_dict)

        # print(xml_output_employee)
        # 输出 <?xml version='1.0' encoding='utf-8'?>
        #      <Employee><employeeId>2</employeeId><department>Sales</department><position>Manager</position><hireDate>2020-05-01</hireDate></Employee>

        print(XmlDataClassSchema.to_xml(person_instance))


    test_xml_to_class()
    test_calss_to_xml()
