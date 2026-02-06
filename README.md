# 🧠 Slatekore

**AI Research Second Brain Starter Kit for Obsidian + Gemini CLI**

Transform your Obsidian vault into an AI-powered research second brain. Slatekore provides the complete structure, templates, and agent configuration to supercharge your research workflow with Gemini CLI.

## ⚡ Quick Start

### Prerequisites

1. **Obsidian** with these plugins installed:
   - [Terminal](https://github.com/polyipseity/obsidian-terminal) - CLI access within Obsidian
   - [Calendar](https://github.com/liamcain/obsidian-calendar-plugin) - Daily notes visualization
   - [CardBoard](https://github.com/roovo/obsidian-card-board) - Kanban task management

2. **Gemini CLI** installed and configured:
   ```bash
   # Follow: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart
   ```

### Install Slatekore

```bash
# Option 1: Persistent installation (recommended)
uv tool install slatekore --from git+https://github.com/mirsakib/slatekore.git

# Option 2: One-time usage
uvx --from git+https://github.com/mirsakib/slatekore.git slatekore init .
```

### Initialize Your Vault

```bash
# In a new vault
slatekore init /path/to/vault

# Or in current directory
cd /path/to/vault
slatekore init .

# Force overwrite existing config
slatekore init . --force
```

## 📁 What Gets Created

```
your-vault/
├── GEMINI.md                    # AI agent configuration
├── .agent/workflows/            # Slash command workflows
├── .obsidian/templates/         # 12 note templates
├── 00-Inbox/                    # Temporary holding area
├── 01-Projects/                 # Active research projects
├── 02-Papers/                   # Research paper notes
├── 03-Codebases/                # GitHub repos
├── 04-Concepts/                 # Atomic concept notes
├── 05-Books/                    # Book notes
├── 06-Resources/                # PDFs, videos, datasets
├── 07-Daily/                    # Daily notes
├── 08-Maps/                     # Maps of Content
├── 09-Models/                   # HuggingFace models
├── 10-Implementations/          # HuggingFace Spaces
├── 11-Datasets/                 # Dataset documentation
└── 12-Websites/                 # Project pages, blogs
```

## 🤖 Using with Gemini CLI

Open Terminal in Obsidian and run:

```bash
gemini
```

Then use these workflows:

| Command | Description |
|---------|-------------|
| `/capture <url>` | Capture any URL (ArXiv, HuggingFace, GitHub, YouTube) |
| `/daily-setup` | Create today's daily note with tasks |
| `/daily-digest` | End-of-day summary and review |
| `/explore <topic>` | Research a topic across your vault |
| `/connect [[note]]` | Find connections for a note |
| `/moc-create <topic>` | Create Map of Content |
| `/project-create <name>` | Create full project structure |

## 📝 Templates Included

- **paper_template.md** - ArXiv paper notes
- **model_template.md** - HuggingFace model notes
- **repo_template.md** - GitHub repository notes
- **space_template.md** - HuggingFace Space notes
- **dataset_template.md** - Dataset documentation
- **website_template.md** - Website/blog captures
- **video_template.md** - YouTube video analysis
- **project_template.md** - Project overview
- **prd_template.md** - Product Requirements Document
- **system-design_template.md** - System architecture
- **daily_template.md** - Daily notes
- **moc_template.md** - Maps of Content

## 🔧 CLI Reference

```bash
# Initialize vault
slatekore init <path>
slatekore init .
slatekore init . --force

# Check prerequisites
slatekore check

# Update templates (coming soon)
slatekore upgrade
```

## 📖 Workflows

### Morning Routine
1. Open terminal: `gemini`
2. Run: `/daily-setup`
3. Review tasks and focus

### Capturing Research
1. Find paper/model/repo
2. Run: `/capture <url>`
3. Review and add insights

### End of Day
1. Run: `/daily-digest`
2. Review progress
3. Plan tomorrow

## 🏗️ Creating Projects

When you run `/project-create <name>`, this creates:

```
01-Projects/<name>/
├── project.md          # Main project note
├── prd.md              # Product Requirements
├── system-design.md    # Architecture
├── kanban.md           # Task board
└── specs/              # Technical specs
```

## 📄 License

MIT

## 🙏 Acknowledgements

Inspired by [spec-kit](https://github.com/github/spec-kit) and the Zettelkasten method.
