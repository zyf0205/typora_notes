#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
笔记分析工具 (Notes Analysis Tool)
分析Typora笔记仓库的内容统计和主题分类
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime


class NotesAnalyzer:
    """笔记分析器类"""
    
    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)
        self.notes = []
        self.stats = {
            "total_notes": 0,
            "total_lines": 0,
            "total_words": 0,
            "total_chars": 0,
            "topics": defaultdict(list)
        }
    
    def find_markdown_files(self):
        """查找所有markdown文件"""
        for md_file in self.repo_path.rglob("*.md"):
            # 跳过 .git 目录、README.md 和分析报告本身
            if ".git" in str(md_file):
                continue
            if md_file.name == "README.md" and md_file.parent == self.repo_path:
                continue
            if md_file.name == "笔记分析报告.md":
                continue
            self.notes.append(md_file)
        return self.notes
    
    def analyze_file(self, file_path):
        """分析单个文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            words = len(re.findall(r'\S+', content))
            chars = len(content)
            
            # 提取标题
            headers = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
            
            # 提取代码块
            code_blocks = re.findall(r'```[\s\S]*?```', content)
            
            # 提取图片
            images = re.findall(r'!\[.*?\]\(.*?\)', content)
            
            return {
                "path": file_path,
                "lines": len(lines),
                "words": words,
                "chars": chars,
                "headers": headers,
                "code_blocks": len(code_blocks),
                "images": len(images)
            }
        except Exception as e:
            print(f"读取文件 {file_path} 时出错: {e}")
            return None
    
    def categorize_by_topic(self):
        """按主题分类笔记"""
        for note in self.notes:
            # 获取相对路径的第一级目录作为主题
            relative_path = note.relative_to(self.repo_path)
            if len(relative_path.parts) > 1:
                topic = relative_path.parts[0]
            else:
                topic = "根目录"
            self.stats["topics"][topic].append(note)
    
    def generate_report(self):
        """生成分析报告"""
        # 查找所有笔记
        self.find_markdown_files()
        self.categorize_by_topic()
        
        # 分析每个笔记
        detailed_analysis = []
        for note in self.notes:
            analysis = self.analyze_file(note)
            if analysis:
                detailed_analysis.append(analysis)
                self.stats["total_lines"] += analysis["lines"]
                self.stats["total_words"] += analysis["words"]
                self.stats["total_chars"] += analysis["chars"]
        
        self.stats["total_notes"] = len(self.notes)
        
        # 生成报告文本
        report = []
        report.append("# 📊 笔记分析报告\n")
        report.append(f"**生成时间**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}\n")
        report.append("---\n")
        
        # 总体统计
        report.append("## 📈 总体统计\n")
        report.append(f"- **笔记总数**: {self.stats['total_notes']} 篇")
        report.append(f"- **总行数**: {self.stats['total_lines']:,} 行")
        report.append(f"- **总字数**: {self.stats['total_words']:,} 字")
        report.append(f"- **总字符数**: {self.stats['total_chars']:,} 字符")
        report.append(f"- **平均每篇笔记**: {self.stats['total_lines']//self.stats['total_notes'] if self.stats['total_notes'] > 0 else 0} 行\n")
        
        # 主题分类统计
        report.append("## 📚 主题分类统计\n")
        report.append("| 主题 | 笔记数量 | 占比 |")
        report.append("|------|---------|------|")
        
        sorted_topics = sorted(self.stats["topics"].items(), key=lambda x: len(x[1]), reverse=True)
        for topic, notes in sorted_topics:
            percentage = len(notes) / self.stats["total_notes"] * 100
            report.append(f"| {topic} | {len(notes)} 篇 | {percentage:.1f}% |")
        report.append("")
        
        # 详细笔记列表
        report.append("## 📝 详细笔记列表\n")
        
        # 按主题分组显示
        for topic, notes in sorted_topics:
            report.append(f"### {topic}\n")
            for note in notes:
                analysis = next((a for a in detailed_analysis if a["path"] == note), None)
                if analysis:
                    relative_path = note.relative_to(self.repo_path)
                    report.append(f"**{note.name}**")
                    report.append(f"- 路径: `{relative_path}`")
                    report.append(f"- 行数: {analysis['lines']} | 字数: {analysis['words']} | 代码块: {analysis['code_blocks']} | 图片: {analysis['images']}")
                    if analysis['headers']:
                        report.append(f"- 主要章节: {', '.join(analysis['headers'][:5])}")
                        if len(analysis['headers']) > 5:
                            report.append(f"  (还有 {len(analysis['headers']) - 5} 个章节...)")
                    report.append("")
        
        # 最详细的笔记（Top 5）
        report.append("## 🏆 最详细的笔记 (Top 5)\n")
        top_notes = sorted(detailed_analysis, key=lambda x: x["lines"], reverse=True)[:5]
        for i, note in enumerate(top_notes, 1):
            relative_path = note["path"].relative_to(self.repo_path)
            report.append(f"{i}. **{note['path'].name}** (`{relative_path}`)")
            report.append(f"   - {note['lines']} 行 | {note['words']} 字 | {note['code_blocks']} 代码块\n")
        
        # 内容特征分析
        report.append("## 🔍 内容特征分析\n")
        total_code_blocks = sum(a["code_blocks"] for a in detailed_analysis)
        total_images = sum(a["images"] for a in detailed_analysis)
        report.append(f"- **代码块总数**: {total_code_blocks} 个")
        report.append(f"- **图片总数**: {total_images} 张")
        report.append(f"- **平均每篇笔记代码块数**: {total_code_blocks/self.stats['total_notes']:.1f} 个")
        report.append(f"- **平均每篇笔记图片数**: {total_images/self.stats['total_notes']:.1f} 张\n")
        
        # 学习建议
        report.append("## 💡 学习建议\n")
        report.append("基于笔记分析，以下是一些建议：\n")
        
        if len(sorted_topics) > 0:
            top_topic = sorted_topics[0][0]
            report.append(f"1. **主要学习方向**: 目前 `{top_topic}` 是你的主要学习领域，建议继续深入学习")
        
        avg_lines = self.stats['total_lines'] / self.stats['total_notes'] if self.stats['total_notes'] > 0 else 0
        if avg_lines < 50:
            report.append("2. **笔记深度**: 当前笔记相对简洁，可以考虑添加更多实例和详细说明")
        else:
            report.append("2. **笔记深度**: 笔记内容较为充实，保持这个良好的记录习惯")
        
        if total_code_blocks / self.stats['total_notes'] > 2:
            report.append("3. **代码实践**: 笔记中包含大量代码示例，说明注重实践，非常好！")
        
        report.append("4. **持续更新**: 建议定期回顾和更新笔记，巩固学习成果\n")
        
        # 结束语
        report.append("---\n")
        report.append("*此报告由笔记分析工具自动生成* 📊\n")
        
        return "\n".join(report)
    
    def save_report(self, output_file="笔记分析报告.md"):
        """保存报告到文件"""
        report = self.generate_report()
        output_path = self.repo_path / output_file
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ 分析报告已生成: {output_path}")
        return output_path


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="📊 笔记分析工具 - 分析Typora笔记仓库的内容统计和主题分类",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python3 analyze_notes.py                    # 分析当前目录的笔记
  python3 analyze_notes.py -o report.md       # 指定输出文件名
  python3 analyze_notes.py -p /path/to/notes  # 指定笔记目录

生成的报告包含：
  ✓ 笔记总数、行数、字数等统计
  ✓ 主题分类和分布
  ✓ 详细笔记列表
  ✓ 内容特征分析
  ✓ 学习建议
        """
    )
    
    parser.add_argument(
        "-p", "--path",
        default=".",
        help="笔记目录路径 (默认: 当前目录)"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="笔记分析报告.md",
        help="输出报告文件名 (默认: 笔记分析报告.md)"
    )
    
    args = parser.parse_args()
    
    print("🔍 开始分析笔记...")
    analyzer = NotesAnalyzer(args.path)
    analyzer.save_report(args.output)
    print("✨ 分析完成！")


if __name__ == "__main__":
    main()
