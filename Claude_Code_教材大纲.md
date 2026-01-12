# Claude Code 从入门到精通 - 教材大纲
## 面向高校行政教师的智能办公助手实战指南

> 🎓 **写在前面的话**
> 嘿，各位老师好！我是你们的"学长"，有 20 年编程经验的老司机。
> 这份教材不是那种让人打瞌睡的技术文档，而是像咱们一起喝咖啡聊天一样，
> 手把手教你用 Claude Code 这个"AI 小助手"来搞定高校办公中的各种琐事。
> 别怕命令行，别怕配置，跟着我，包你三天变大神！💪

---

## 📚 教材结构总览

本教材共分为 **8 大章节**，从零基础到进阶应用，循序渐进：

```
第一章：破冰之旅 - Claude Code 是个啥？
第二章：安装大作战 - 3 分钟搞定环境
第三章：新手村任务 - 第一次对话就上手
第四章：技能树解锁 - Skills 让你事半功倍
第五章：召唤神兽 - SubAgents 并行处理任务
第六章：魔法钩子 - Hooks 自动化你的工作流
第七章：外挂系统 - MCP 服务器连接万物
第八章：大师进阶 - 综合案例与最佳实践
```

---

## 第一章：破冰之旅 - Claude Code 是个啥？

### 1.1 一句话讲清楚：你的超级 AI 秘书
- **不是什么**：不是又一个聊天机器人
- **是什么**：能看懂你代码、帮你写文档、自动处理任务的"命令行里的 AI 助手"
- **大白话解释**：就像给你的电脑装了个懂你心思的小助理

### 1.2 高校行政老师为啥要学这个？
- **场景 1**：每学期要做几十个 Excel 报表？Claude 帮你批量处理
- **场景 2**：写通知公告累成狗？Claude 帮你生成规范文档
- **场景 3**：整理学生信息头大？Claude 帮你数据清洗
- **场景 4**：Git 管理文档版本？Claude 帮你自动提交
- **真实案例**：某高校行政老师用 Claude Code 把月报生成时间从 2 天缩短到 2 小时

### 1.3 学完能干啥？能力清单
- ✅ 自动化处理重复性工作
- ✅ 批量生成各类文档和表格
- ✅ 管理和同步文件版本（Git）
- ✅ 数据分析和可视化
- ✅ 创建自定义办公工具
- ✅ 团队协作效率翻倍

### 1.4 学习路线图
```
入门阶段（1-3 天）→ 掌握基础命令
进阶阶段（1 周）  → 自定义 Skills 和 SubAgents
高级阶段（2 周）  → 构建自动化工作流
大师阶段（1 个月）→ 团队推广和最佳实践
```

---

## 第二章：安装大作战 - 3 分钟搞定环境

### 2.1 系统要求检查（别慌，很简单）
- **Windows 用户**：Windows 10/11 即可
- **Mac 用户**：macOS 10.15+ 即可
- **Linux 用户**：你都用 Linux 了还怕啥？😎

### 2.2 三种安装方法，总有一种适合你

#### 方法 1：一键安装（最推荐，5 岁小孩都会）
**Windows 系统：**
```powershell
# 复制这行，在 PowerShell 里粘贴，回车，搞定！
irm https://claude.ai/install.ps1 | iex
```
**Mac/Linux 系统：**
```bash
# 复制这行，在终端里粘贴，回车，搞定！
curl -fsSL https://claude.ai/install.sh | bash
```

#### 方法 2：用包管理器安装（Mac 用户的福音）
```bash
# Mac 用户用 Homebrew
brew install --cask claude-code
```

#### 方法 3：用 NPM 安装（程序员友好）
```bash
# 需要先装 Node.js（18+）
npm install -g @anthropic-ai/claude-code
```

### 2.3 验证安装成功
```bash
# 在命令行输入这个，看到版本号就成功了！
claude --version
```

### 2.4 首次运行配置
- **API Key 获取**：一步步截图教学
- **账号绑定**：微信扫码就行（假设国内版）
- **常见报错**：5 大报错及解决方案

### 2.5 实战演练：第一次启动
```bash
# 进入你的工作目录
cd ~/Documents/MyOfficeWork

# 启动 Claude Code
claude

# 看到这个界面就成功了！
>>
```

---

## 第三章：新手村任务 - 第一次对话就上手

### 3.1 基础对话：让 AI 听懂人话
**案例 1：生成学期工作计划**
```
>> 帮我生成一份 2026 年春季学期行政办公室工作计划
```
- 📌 学习点：如何用自然语言描述需求
- 📌 学习点：Claude 如何理解上下文

**案例 2：整理会议纪要**
```
>> 我有一份录音转文字的会议记录，帮我整理成规范的会议纪要格式
```
- 📌 学习点：文件读取和处理
- 📌 学习点：格式化输出

### 3.2 文件操作：读、写、改
**案例 3：批量重命名文件**
```
>> 把这个文件夹里的所有 Excel 文件按照"年份-月份-报表名称"格式重命名
```
- 📌 学习点：Glob 工具查找文件
- 📌 学习点：Bash 工具执行命令

**案例 4：生成 Excel 报表**
```
>> 读取 students.csv，按照班级统计人数，生成 Excel 报表
```
- 📌 学习点：数据处理流程
- 📌 学习点：Python 脚本自动生成

### 3.3 常用命令速查表
| 命令 | 作用 | 示例 |
|------|------|------|
| `/help` | 查看帮助 | `/help` |
| `/list` | 列出当前会话文件 | `/list` |
| `/clear` | 清空对话 | `/clear` |
| `/exit` | 退出 | `/exit` |
| `/bug` | 报告问题 | `/bug 出现了 XX 错误` |

### 3.4 Git 集成：版本管理不再难
**案例 5：自动提交文档更改**
```
>> 帮我把刚才修改的工作计划提交到 Git，commit 信息写"更新春季学期计划"
```
- 📌 学习点：Git 基础概念
- 📌 学习点：Claude 自动化 Git 流程

### 3.5 实战演练：完成第一个办公任务
**综合案例：生成学生信息统计报告**
- 需求：读取学生名单 CSV，按性别、年级统计，生成 Word 文档
- 步骤详解：从对话到生成最终文档
- 常见问题：格式调整、中文乱码解决

---

## 第四章：技能树解锁 - Skills 让你事半功倍

### 4.1 什么是 Skills？（一个比喻搞懂）
- **比喻**：Skills 就像游戏里的"技能书"，学一次，永久使用
- **官方定义**：可复用的能力扩展，跨项目共享
- **大白话**：把你常用的操作打包成一键命令

### 4.2 Skills 的三大类型
1. **自己写的 Skills**：针对你的工作定制
2. **社区 Skills**：别人写好的，拿来就用
3. **插件 Skills**：官方或第三方提供

### 4.3 创建你的第一个 Skill
**案例 6：一键生成通知公告**

#### Step 1：创建 Skill 文件夹
```bash
mkdir -p ~/.claude/skills/notice-generator
```

#### Step 2：编写 SKILL.md
```markdown
---
name: notice-generator
description: 生成规范的高校通知公告
tools: Read, Write
model: sonnet
---

你是高校行政办公室的文秘专家，擅长撰写规范的通知公告。

当用户调用此技能时：
1. 询问通知类型（会议通知、活动通知、放假通知等）
2. 询问关键信息（时间、地点、事项等）
3. 按照高校公文格式生成通知
4. 包含：标题、正文、落款、日期

格式要求：
- 标题居中，加粗
- 称呼规范（各部门、各位师生等）
- 正文段落清晰
- 落款右对齐
```

#### Step 3：使用 Skill
```
>> 使用 notice-generator 生成一份期末考试安排通知
```

### 4.4 高校办公常用 Skills 库
**预设 10 个实用 Skills，开箱即用：**

1. **excel-processor** - Excel 批量处理
2. **meeting-minutes** - 会议纪要生成
3. **student-analyzer** - 学生数据分析
4. **document-formatter** - 文档格式化
5. **email-drafter** - 邮件起草助手
6. **schedule-maker** - 课表/值班表生成
7. **data-validator** - 数据校验工具
8. **report-generator** - 报表生成器
9. **file-organizer** - 文件整理归档
10. **backup-manager** - 备份管理工具

### 4.5 进阶：Skills 的高级配置
- **FORMS.md**：创建交互式表单
- **REFERENCE.md**：添加 API 文档
- **scripts/**：集成自定义脚本

**案例 7：带表单的学生信息录入 Skill**
- 配置 FORMS.md 定义字段
- 自动校验数据格式
- 导出为标准 Excel 模板

### 4.6 Skills 管理命令
```bash
# 列出所有已安装 Skills
claude skills list

# 安装社区 Skill
claude skills add <skill-name>

# 删除 Skill
claude skills remove <skill-name>
```

---

## 第五章：召唤神兽 - SubAgents 并行处理任务

### 5.1 SubAgent 是什么？（脑洞大开的解释）
- **比喻**：就像《火影忍者》里的影分身，同时干多件事
- **技术解释**：独立运行的 AI 实例，各司其职
- **为啥牛逼**：10 个任务并行处理，效率爆表

### 5.2 SubAgent vs Skills vs 主对话
| 对比项 | 主对话 | Skills | SubAgents |
|--------|--------|--------|-----------|
| 运行方式 | 主线程 | 主线程 | 独立线程 |
| 并发能力 | ❌ | ❌ | ✅（最多 10 个） |
| 适用场景 | 简单任务 | 可复用任务 | 复杂/多步骤任务 |
| 上下文 | 共享 | 共享 | 隔离 |

### 5.3 创建你的第一个 SubAgent
**案例 8：代码审查助手**

#### Step 1：创建 SubAgent 文件
```bash
mkdir -p ~/.claude/agents
nano ~/.claude/agents/code-reviewer.md
```

#### Step 2：编写配置
```markdown
---
name: code-reviewer
description: 专业代码审查员，自动检查代码质量。用于代码变更后。
tools: Read, Grep, Glob, Bash
model: sonnet
permissionMode: default
---

你是资深代码审查专家，关注代码质量、安全性、最佳实践。

被调用时：
1. 运行 git diff 查看最近改动
2. 聚焦修改的文件
3. 立即开始审查

审查清单：
- 代码清晰易读
- 无重复代码
- 错误处理完善
- 无敏感信息泄露
- 输入验证完整
- 测试覆盖充分

按优先级组织反馈：关键、警告、建议。
```

### 5.4 高校办公场景的 SubAgents 全家桶
**预设 8 个办公 SubAgents：**

1. **data-analyst** - 数据分析师
   - 工具：Python, Pandas, Matplotlib
   - 场景：学生成绩分析、招生数据统计

2. **document-processor** - 文档处理专家
   - 工具：Word, Excel, PDF
   - 场景：批量生成证明、合并文档

3. **schedule-optimizer** - 排课优化师
   - 工具：算法库
   - 场景：自动排课、避免冲突

4. **email-assistant** - 邮件管家
   - 工具：邮件客户端
   - 场景：批量发送通知、跟进回复

5. **backup-guardian** - 备份守护者
   - 工具：Git, rsync
   - 场景：自动备份重要文件

6. **report-compiler** - 报表编译器
   - 工具：数据库、Excel
   - 场景：月报、年报自动生成

7. **debugger** - 问题解决专家
   - 工具：全工具集
   - 场景：修复脚本错误、调试流程

8. **research-assistant** - 资料研究员
   - 工具：Web 搜索、文档读取
   - 场景：政策查询、文献整理

### 5.5 使用 SubAgent 的三种方式
**方式 1：自动委托（最智能）**
```
>> 分析一下今年的招生数据趋势
[Claude 自动调用 data-analyst SubAgent]
```

**方式 2：显式调用**
```
>> 用 data-analyst 子代理分析 enrollment.xlsx
```

**方式 3：并行执行**
```
>> 同时让 data-analyst 分析招生数据，
   让 report-compiler 生成月报，
   让 backup-guardian 备份所有文件
```

### 5.6 实战案例：期末成绩处理流水线
**需求**：
- 读取 500 名学生成绩
- 数据清洗（去重、补缺）
- 统计分析（平均分、及格率）
- 生成可视化图表
- 导出 Excel 和 PDF 报告

**解决方案**：
- 用 3 个 SubAgent 并行处理
- 流程详解 + 代码示例

### 5.7 SubAgent 进阶配置
- **permissionMode**：权限模式详解
  - `default`：标准权限
  - `acceptEdits`：自动接受编辑
  - `bypassPermissions`：跳过权限检查（慎用）
- **hooks**：生命周期钩子
- **前后台切换**：Ctrl+B 快捷键

---

## 第六章：魔法钩子 - Hooks 自动化你的工作流

### 6.1 Hooks 是什么？（一个魔法故事）
- **比喻**：就像《哈利波特》里的咒语，触发就自动执行
- **技术定义**：事件驱动的自动化脚本
- **生活例子**：每次保存文件自动备份，就是一个 Hook

### 6.2 Hooks 的 5 大触发时机
| 事件 | 触发时机 | 典型用途 |
|------|----------|----------|
| `PreToolUse` | 工具使用前 | 权限检查、参数验证 |
| `PostToolUse` | 工具使用后 | 代码格式化、自动提交 |
| `SessionStart` | 会话启动时 | 环境初始化、加载配置 |
| `SubagentStart` | 子代理启动时 | 设置专用环境 |
| `SubagentStop` | 子代理停止时 | 清理临时文件 |

### 6.3 创建你的第一个 Hook
**案例 9：每次编辑文档后自动备份**

#### Step 1：创建 settings.json
```bash
mkdir -p ~/Documents/MyOfficeWork/.claude
nano ~/Documents/MyOfficeWork/.claude/settings.json
```

#### Step 2：配置 Hook
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "cp $FILE_PATH ./backups/$(date +%Y%m%d_%H%M%S)_$FILE_NAME"
          }
        ]
      }
    ]
  }
}
```

### 6.4 高校办公常用 Hooks 合集
**Hooks 1：自动 Git 提交**
```json
{
  "PostToolUse": [{
    "matcher": "Edit|Write",
    "hooks": [{
      "type": "command",
      "command": "git add . && git commit -m '自动保存: $(date)'"
    }]
  }]
}
```

**Hooks 2：文档格式化**
```json
{
  "PostToolUse": [{
    "matcher": "Write",
    "hooks": [{
      "type": "command",
      "command": "./scripts/format-document.sh $FILE_PATH"
    }]
  }]
}
```

**Hooks 3：会话启动时加载模板**
```json
{
  "SessionStart": [{
    "hooks": [{
      "type": "command",
      "command": "echo '欢迎使用办公助手！已加载常用模板。'"
    }]
  }]
}
```

### 6.5 实战案例：全自动月报生成系统
**需求**：每月 1 号自动生成上月工作报告

**解决方案**：
1. SessionStart Hook 检查日期
2. 触发 report-compiler SubAgent
3. 读取数据源（考勤、会议、项目等）
4. 生成 Word 报告
5. 自动发送邮件给领导
6. 备份到网盘

**完整代码示例 + 部署指南**

### 6.6 Hooks 调试技巧
- 查看 Hook 执行日志
- 常见错误排查
- 权限问题解决

---

## 第七章：外挂系统 - MCP 服务器连接万物

### 7.1 MCP 是什么？（大白话版）
- **官方说法**：Model Context Protocol，AI 工具集成开放标准
- **人话版**：让 Claude 能连接各种外部服务（数据库、网盘、邮箱等）
- **举例**：就像给手机装 APP，装什么能力就有什么

### 7.2 MCP 服务器生态图谱
```
Claude Code
    ├── 文件系统 MCP（本地文件）
    ├── 数据库 MCP（MySQL, PostgreSQL）
    ├── 网盘 MCP（Dropbox, Google Drive）
    ├── 办公套件 MCP（腾讯文档、WPS）
    ├── 邮件 MCP（SMTP, IMAP）
    └── 自定义 MCP（你自己开发）
```

### 7.3 安装你的第一个 MCP 服务器
**案例 10：连接 Excel 数据源**

#### Step 1：添加 MCP 服务器
```bash
claude mcp add \
  --transport stdio \
  excel-mcp \
  -- npx -y @modelcontextprotocol/server-excel
```

#### Step 2：验证安装
```bash
claude mcp list
```

#### Step 3：使用 MCP
```
>> 读取 D:/Documents/students.xlsx 的第一个 sheet，显示前 10 行
```

### 7.4 高校办公必备 MCP 服务器
**推荐安装清单：**

1. **Filesystem MCP** - 高级文件操作
2. **PostgreSQL MCP** - 学生信息管理系统对接
3. **Google Drive MCP** - 云盘同步
4. **Email MCP** - 邮件自动化
5. **Calendar MCP** - 日程管理
6. **Web Search MCP** - 政策文件查询

### 7.5 实战案例：对接学校教务系统
**需求**：从教务系统数据库提取学生成绩

**步骤详解：**
1. 配置数据库 MCP
2. 编写查询 SQL
3. Claude 自动提取数据
4. 生成分析报告

**安全提醒：**
- 密钥管理最佳实践
- 权限最小化原则

### 7.6 自定义 MCP 服务器开发（进阶）
- MCP 协议简介
- 开发一个简单的 MCP（示例：校园卡查询）
- 发布到 MCP 仓库

---

## 第八章：大师进阶 - 综合案例与最佳实践

### 8.1 综合案例 1：全自动招生数据分析系统
**业务流程：**
1. 从教务系统导出招生数据
2. 数据清洗和去重
3. 按省份/专业/分数段统计
4. 生成可视化图表（饼图、柱状图、趋势图）
5. 撰写分析报告（Word）
6. 自动发送邮件给招生办领导

**技术方案：**
- MCP：连接教务系统数据库
- SubAgent：data-analyst 并行处理
- Skill：report-generator 生成报告
- Hook：自动备份和邮件发送

**完整代码 + 部署文档**

### 8.2 综合案例 2：智能排课系统
**需求分析：**
- 输入：教师列表、课程列表、教室列表、时间段
- 约束：教师不冲突、教室容量、连堂课安排
- 输出：最优课表（Excel + 可视化）

**技术实现：**
- SubAgent：schedule-optimizer（遗传算法）
- Skill：constraint-checker（约束检查）
- Hook：每次调整自动保存版本

**实战演练：为 50 个班级排课**

### 8.3 综合案例 3：期末工作流水线
**一键完成期末所有工作：**
1. 成绩录入和校验
2. 补考名单生成
3. 成绩单打印（批量 PDF）
4. 档案归档（自动分类）
5. 总结报告撰写
6. 备份到云盘

**技术栈：**
- 5 个 SubAgents 并行
- 10+ Hooks 自动化
- 3 个 MCP 服务器
- 自定义 Skills

### 8.4 团队协作最佳实践
**场景：办公室 5 个人共享配置**

#### 8.4.1 项目级配置管理
```bash
MyOfficeWork/
├── .claude/
│   ├── agents/          # 共享 SubAgents
│   ├── skills/          # 共享 Skills
│   ├── settings.json    # 团队配置
│   └── CLAUDE.md        # 项目说明
├── data/                # 数据目录
├── scripts/             # 自动化脚本
└── templates/           # 文档模板
```

#### 8.4.2 Git 工作流
```bash
# 团队成员 A 创建新 Skill
git checkout -b feature/new-skill
# 编写完成后提交
git add .claude/skills/new-skill/
git commit -m "新增学生信息校验 Skill"
git push

# 团队成员 B 拉取更新
git pull
# 自动获得新 Skill
```

### 8.5 性能优化技巧
1. **减少 token 消耗**：精简提示词、限制上下文
2. **并行任务调度**：SubAgents 最佳数量（3-5 个）
3. **缓存策略**：重复查询用本地缓存
4. **模型选择**：简单任务用 Haiku，复杂任务用 Sonnet

### 8.6 安全与隐私
- **敏感数据处理**：加密存储、定期清理
- **API Key 管理**：环境变量、密钥轮换
- **权限控制**：最小权限原则
- **审计日志**：记录所有自动化操作

### 8.7 故障排查手册
**常见问题 Top 10：**
1. Claude 无响应 → 检查网络和 API 配额
2. 文件找不到 → 检查路径和权限
3. Hook 不执行 → 检查 matcher 正则
4. SubAgent 冲突 → 减少并发数量
5. MCP 连接失败 → 检查服务器状态
6. 中文乱码 → 设置 UTF-8 编码
7. Git 提交失败 → 检查配置和权限
8. 生成文档格式错误 → 调整模板
9. 性能慢 → 优化提示词和并发
10. 更新后出错 → 回滚版本

### 8.8 社区资源
- **官方文档**：https://code.claude.com/docs
- **GitHub 仓库**：https://github.com/anthropics/claude-code
- **社区论坛**：Discord / 知乎 / CSDN
- **示例项目**：awesome-claude-code
- **插件市场**：claudedirectory.org

### 8.9 持续学习路线
1. **初级阶段**：完成本教材所有案例（2 周）
2. **中级阶段**：开发 5 个自定义 Skills（1 个月）
3. **高级阶段**：构建部门级自动化系统（2 个月）
4. **专家阶段**：贡献开源、分享经验（持续）

### 8.10 结语：从工具到思维
> **学长寄语：**
> Claude Code 不只是个工具，它代表了一种新的工作方式：
> **从重复劳动到创造性工作**
> **从被动响应到主动优化**
> **从个人效率到团队赋能**
>
> 希望这份教材能帮你开启 AI 办公的新世界！
> 记住：最好的学习方法就是动手实践！
> 有问题随时来社区找我们 🤝

---

## 📖 附录

### 附录 A：命令速查表
完整的 Claude Code 命令列表和参数说明

### 附录 B：配置文件模板
- settings.json 完整模板
- SKILL.md 标准模板
- Agent.md 标准模板

### 附录 C：正则表达式快速入门
Hook matcher 中使用的正则语法

### 附录 D：常用脚本库
30+ 开箱即用的自动化脚本

### 附录 E：术语表
中英文对照、技术术语解释

### 附录 F：学习资源推荐
- 在线课程
- 推荐书籍
- 优秀博客
- YouTube 频道

---

## 🎯 教材使用说明

### 面向教师的教学建议
1. **课时安排**：建议 16 学时（8 次课，每次 2 小时）
2. **教学方式**：50% 理论 + 50% 实操
3. **考核方式**：完成 3 个综合案例
4. **课后作业**：每章配套练习题

### 面向学习者的自学指南
1. **学习节奏**：每天 1-2 小时，2 周完成
2. **实践为主**：每个案例都动手做
3. **记录笔记**：建立自己的知识库
4. **参与社区**：遇到问题及时求助

### 配套资源
- **视频教程**：B站/YouTube 同步更新
- **示例代码**：GitHub 仓库托管
- **练习题库**：在线测试平台
- **答疑群组**：微信群/Discord

---

**版本信息：**
- 教材版本：v1.0
- 发布日期：2026-01-12
- 基于 Claude Code 版本：2.1.3
- 作者：20 年编程经验的资深技术专家
- 许可证：CC BY-NC-SA 4.0（署名-非商业性使用-相同方式共享）

**更新计划：**
- 每季度更新一次，跟进最新功能
- 持续补充社区优秀案例
- 根据读者反馈优化内容

---

## 📚 参考资料与延伸阅读

### 官方文档
- [Claude Code CLI 官方文档](https://code.claude.com/docs/en/cli-reference)
- [Claude Code GitHub 仓库](https://github.com/anthropics/claude-code)
- [Claude Code 更新日志](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

### 中文资源
- [Claude Code 子代理文档（中文）](https://code.claude.com/docs/zh-CN/sub-agents)
- [MCP 服务器配置（中文）](https://code.claude.com/docs/zh-CN/mcp)

### 社区资源
- [awesome-claude-code - 精选命令和工作流](https://github.com/hesreallyhim/awesome-claude-code)
- [claude-code-showcase - 综合配置示例](https://github.com/ChrisWiles/claude-code-showcase)
- [awesome-claude-code-subagents - 100+ 子代理集合](https://github.com/VoltAgent/awesome-claude-code-subagents)

### 技术博客
- [Claude Code 五件套完全解析](https://zhuanlan.zhihu.com/p/1966486877088506681)
- [Subagent 与 Skill 核心区别](https://www.cnblogs.com/gyc567/p/19185954)
- [Claude Code 自定义指南](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/)
- [Claude Code 使用技巧实测](https://www.cnblogs.com/jinjiangongzuoshi/p/19424468)

### 实战案例
- [Claude Code 深度实战指南](https://aicoding.csdn.net/68872aac080e555a88d2f7f7.html)
- [Claude Code 2.1 新功能详解](https://mlearning.substack.com/p/claude-code-21-new-features-january-2026)
- [我如何使用 Claude Code 的每个功能](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)

### 工具网站
- [Claude Directory - 插件和配置目录](https://www.claudedirectory.org/)
- [MCP 服务器目录](https://mcpdir.dev/)
- [LobeHub MCP 服务器集合](https://lobehub.com/mcp)

---

**结束语**

这份大纲覆盖了从零基础到精通的完整学习路径，每一章都配有真实的高校办公场景案例。

通过风趣幽默的讲解方式，让原本枯燥的技术学习变得生动有趣。

记住：**工具在手，效率我有！跟着学长，走向巅峰！** 💪🚀

---

© 2026 Claude Code 从入门到精通教材组
为高校行政教师量身打造 🎓
