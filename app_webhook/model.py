from dataclasses import dataclass
import datetime


@dataclass
class MessageContent:
    summary: str
    title: str
    repo: str
    branch: str
    user: str
    state: bool
    log: str
    commit: int

    def state_text(self):
        return "成功" if self.state else "失败"

    def published_at(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"""### {self.title}   
**仓库：** {self.repo}   
**分支：** {self.branch}   
**作者：** {self.user}   
**时间：** {self.published_at()}   
**状态：** {self.state_text()}   
**文件更改数量：** {self.commit}   
**更新命令日志：**
\n> {self.log}
"""
