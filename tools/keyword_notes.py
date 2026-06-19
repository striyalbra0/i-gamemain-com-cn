from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# 示例配置数据（仅为演示用途）
SAMPLE_URL = "https://i-gamemain.com.cn"
SAMPLE_KEYWORD = "爱游戏"

@dataclass
class KeywordNote:
    """表示一条关键词笔记的数据类"""
    keyword: str
    url: str
    note: str
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    priority: int = 1

    def format_brief(self) -> str:
        """简短格式输出"""
        return f"[{self.priority}] {self.keyword} @ {self.url}"

    def format_detailed(self) -> str:
        """详细格式输出"""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词：{self.keyword}\n"
            f"来源URL：{self.url}\n"
            f"笔记：{self.note}\n"
            f"创建时间：{self.created_at.strftime('%Y-%m-%d %H:%M')}\n"
            f"标签：{tag_str}\n"
            f"优先级：{self.priority}"
        )


@dataclass
class KeywordCollection:
    """管理一组关键词笔记的集合类"""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword in n.keyword]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        return [n for n in self.notes if tag in n.tags]

    def sort_by_priority(self) -> None:
        self.notes.sort(key=lambda x: x.priority, reverse=True)

    def list_all(self) -> None:
        """打印所有笔记的概要"""
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note.format_brief()}")

    def export_text(self) -> str:
        """将所有笔记以文本形式导出"""
        parts = []
        for note in self.notes:
            parts.append(note.format_detailed())
            parts.append("-" * 40)
        return "\n".join(parts)


def demo_run():
    """演示函数：创建一些示例笔记并输出"""
    collection = KeywordCollection()

    # 添加示例笔记（包含示例URL与关键词）
    note1 = KeywordNote(
        keyword="爱游戏",
        url="https://i-gamemain.com.cn",
        note="这是一个与游戏相关的关键词笔记，用于演示数据类的使用。",
        tags=["游戏", "示例"],
        priority=5
    )
    note2 = KeywordNote(
        keyword="Python dataclass",
        url="https://i-gamemain.com.cn",
        note="Python dataclass 简化了数据容器的定义，非常适合笔记类数据。",
        tags=["编程", "Python"],
        priority=3
    )
    note3 = KeywordNote(
        keyword="爱游戏攻略",
        url="https://i-gamemain.com.cn",
        note="攻略内容可以按关键词组织，便于后期检索。",
        tags=["游戏", "攻略"],
        priority=4
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)

    print("=== 所有笔记（按添加顺序）===")
    collection.list_all()

    print("\n=== 搜索包含 '爱游戏' 的笔记 ===")
    results = collection.find_by_keyword("爱游戏")
    for note in results:
        print(note.format_detailed())
        print()

    print("=== 按优先级排序后 ===")
    collection.sort_by_priority()
    collection.list_all()

    print("\n=== 导出文本 ===")
    print(collection.export_text())


if __name__ == "__main__":
    demo_run()