"""Vault initialization logic for Slatekore."""

import shutil
from pathlib import Path
from importlib import resources

# Vault folder structure to create
VAULT_FOLDERS = [
    "00-Inbox/papers",
    "00-Inbox/repos",
    "00-Inbox/models",
    "00-Inbox/datasets",
    "00-Inbox/spaces",
    "00-Inbox/websites",
    "01-Projects",
    "02-Papers",
    "03-Codebases",
    "04-Concepts",
    "05-Books",
    "06-Resources/pdfs/papers",
    "06-Resources/pdfs/books",
    "06-Resources/pdfs/reports",
    "06-Resources/videos",
    "06-Resources/datasets",
    "06-Resources/models",
    "07-Daily",
    "08-Maps",
    "09-Models",
    "10-Implementations",
    "11-Datasets",
    "12-Websites",
]


def initialize_vault(target_path: Path, force: bool = False) -> dict:
    """Initialize an Obsidian vault with Slatekore structure.
    
    Args:
        target_path: Path to the vault directory
        force: If True, overwrite existing files
        
    Returns:
        dict with 'created' and 'skipped' lists
    """
    result = {"created": [], "skipped": []}
    
    # Ensure target exists
    target_path.mkdir(parents=True, exist_ok=True)
    
    # 1. Create folder structure
    for folder in VAULT_FOLDERS:
        folder_path = target_path / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            result["created"].append(f"📁 {folder}")
    
    # 2. Create .obsidian/templates directory
    templates_dir = target_path / ".obsidian" / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. Copy template files
    _copy_templates(target_path, force, result)
    
    # 4. Create GEMINI.md (main agent config)
    _create_gemini_config(target_path, force, result)
    
    # 5. Create .agent/workflows directory
    _create_workflows(target_path, force, result)
    
    return result


def _copy_templates(target_path: Path, force: bool, result: dict):
    """Copy all templates to .obsidian/templates/."""
    templates_dir = target_path / ".obsidian" / "templates"
    
    # Get templates from package
    try:
        templates_pkg = resources.files("slatekore.templates.obsidian_templates")
        
        for template_file in templates_pkg.iterdir():
            if template_file.name.endswith(".md"):
                dest = templates_dir / template_file.name
                
                if dest.exists() and not force:
                    result["skipped"].append(f"📄 .obsidian/templates/{template_file.name}")
                else:
                    content = template_file.read_text()
                    dest.write_text(content)
                    result["created"].append(f"📄 .obsidian/templates/{template_file.name}")
    except Exception:
        # Fallback: templates not bundled, create from inline
        _create_inline_templates(templates_dir, force, result)


def _create_inline_templates(templates_dir: Path, force: bool, result: dict):
    """Create templates inline if package resources not available."""
    templates = {
        "paper_template.md": PAPER_TEMPLATE,
        "model_template.md": MODEL_TEMPLATE,
        "repo_template.md": REPO_TEMPLATE,
        "space_template.md": SPACE_TEMPLATE,
        "dataset_template.md": DATASET_TEMPLATE,
        "website_template.md": WEBSITE_TEMPLATE,
        "video_template.md": VIDEO_TEMPLATE,
        "project_template.md": PROJECT_TEMPLATE,
        "prd_template.md": PRD_TEMPLATE,
        "system-design_template.md": SYSTEM_DESIGN_TEMPLATE,
        "daily_template.md": DAILY_TEMPLATE,
        "moc_template.md": MOC_TEMPLATE,
    }
    
    for name, content in templates.items():
        dest = templates_dir / name
        if dest.exists() and not force:
            result["skipped"].append(f"📄 .obsidian/templates/{name}")
        else:
            dest.write_text(content)
            result["created"].append(f"📄 .obsidian/templates/{name}")


def _create_gemini_config(target_path: Path, force: bool, result: dict):
    """Create GEMINI.md in vault root."""
    gemini_path = target_path / "GEMINI.md"
    
    if gemini_path.exists() and not force:
        result["skipped"].append("📝 GEMINI.md")
    else:
        gemini_path.write_text(GEMINI_CONFIG)
        result["created"].append("📝 GEMINI.md")


def _create_workflows(target_path: Path, force: bool, result: dict):
    """Create .agent/workflows/ directory with workflow files."""
    workflows_dir = target_path / ".agent" / "workflows"
    workflows_dir.mkdir(parents=True, exist_ok=True)
    
    workflows = {
        "capture.md": WORKFLOW_CAPTURE,
        "summarize.md": WORKFLOW_SUMMARIZE,
        "daily-setup.md": WORKFLOW_DAILY_SETUP,
        "daily-digest.md": WORKFLOW_DAILY_DIGEST,
        "explore.md": WORKFLOW_EXPLORE,
        "connect.md": WORKFLOW_CONNECT,
        "moc-create.md": WORKFLOW_MOC_CREATE,
        "project-create.md": WORKFLOW_PROJECT_CREATE,
    }
    
    for name, content in workflows.items():
        dest = workflows_dir / name
        if dest.exists() and not force:
            result["skipped"].append(f"📋 .agent/workflows/{name}")
        else:
            dest.write_text(content)
            result["created"].append(f"📋 .agent/workflows/{name}")


# ============================================================================
# INLINE TEMPLATES
# ============================================================================

PAPER_TEMPLATE = '''---
type: paper
source: arxiv
arxiv_id: 
title: 
authors: 
year: 
venue: 
citations: 
created: {{date}}
tags: [#paper, #to-read]
---

# {{title}}

## TL;DR
*One sentence: What problem does this solve and how?*

## Core Contribution
*2-3 sentences on the main innovation*

## Method
### Architecture/Approach

### Key Techniques

### Novel Aspects

## Results
### Main Findings

### Performance Metrics

### Limitations

## Relevance to My Work
### Applicable to Projects
- 

### Implementation Ideas
- 

### Open Questions
- 

## Related Work
### Papers
- 

### Models
- 

### Code
- 

## Resources
- Paper: [arxiv](https://arxiv.org/abs/)
- Code: 
- Model: 
- Dataset: 

## Notes & Insights
### {{date}}
- 
'''

MODEL_TEMPLATE = '''---
type: model
source: huggingface
model_id: 
architecture: 
task: 
license: 
downloads: 
created: {{date}}
tags: [#model, #to-explore]
---

# {{title}}

## Quick Facts
| Property | Value |
|----------|-------|
| Architecture | |
| Parameters | |
| Task | |
| License | |

## Capabilities
*What can this model do?*

## Performance
### Benchmarks

### My Tests

## Architecture Notes
*Key technical details*

## Use Cases for My Work
- 

## Implementation Details
```python
# Example usage
```

## Related
- Papers: 
- Similar Models: 
- Code: 

## Experimentation Log
### {{date}}
- 
'''

REPO_TEMPLATE = '''---
type: repo
source: github
repo_url: 
language: 
stars: 
created: {{date}}
tags: [#code, #to-review]
---

# {{title}}

## Overview
*What does this repo do?*

## Architecture
### Structure

### Key Components

## Novel Techniques
*What's innovative here?*

## Code Patterns Worth Stealing
```
# Useful patterns
```

## Performance Characteristics

## Dependencies & Stack
- 

## Adaptation Ideas
- 

## Related
- Papers: 
- Models: 

## Notes
### {{date}}
- 
'''

SPACE_TEMPLATE = '''---
type: space
source: huggingface
space_id: 
sdk: 
created: {{date}}
tags: [#demo, #to-explore]
---

# {{title}}

## What It Does
*Brief description*

## Demo URL
https://huggingface.co/spaces/

## Implementation Highlights

## Code Analysis
*Key code patterns*

## UX/UI Insights

## Performance

## Adaptation for My Work
- 

## Related
- Models: 
- Papers: 

## Notes
### {{date}}
- 
'''

DATASET_TEMPLATE = '''---
type: dataset
source: huggingface
dataset_id: 
size: 
format: 
license: 
created: {{date}}
tags: [#dataset, #to-explore]
---

# {{title}}

## Overview
*What is this dataset?*

## Access
```python
# How to load
```

## Schema/Structure

## Statistics

## Data Quality
### Strengths

### Issues

### Preprocessing Needed

## Use Cases
- 

## Related
- Papers using this: 
- Models trained on this: 

## Notes
### {{date}}
- 
'''

WEBSITE_TEMPLATE = '''---
type: website
category: 
url: 
org: 
created: {{date}}
tags: [#website, #to-read]
---

# {{title}}

## URL


## Key Takeaways
*Main insights*

## Technical Details

## Novel Ideas

## Code/Resources

## Relevance to My Work

## Follow-up Actions
- 

## Related
- 

## Notes
### {{date}}
- 
'''

VIDEO_TEMPLATE = '''---
type: video
source: youtube
video_id: 
title: 
channel: 
duration: 
published: 
analyzed: {{date}}
tags: [#video, #to-watch]
---

# {{title}}

## Video Information
- **Channel**: 
- **Duration**: 
- **Published**: 
- **URL**: https://youtube.com/watch?v=

## Overview
*What is this video about?*

## Key Topics Covered
### Topic 1 (00:00)

### Topic 2 (00:00)

## Technical Content
### Code Demos

### Architecture/Diagrams

### Tools/Commands

## Key Insights & Learnings
- 

## Resources Referenced
- Papers: 
- Repos: 
- Tools: 

## Practical Applications
- 

## Transcript Highlights
> Key quotes

## Related Content
- 

## Follow-Up Actions
- [ ] 

## Notes
### {{date}}
- 
'''

PROJECT_TEMPLATE = '''---
type: project
status: planning
priority: high
start_date: {{date}}
tags: [#project]
---

# {{project_name}}

## Goal
*What are you trying to achieve?*

## Motivation
*Why does this matter?*

## Status
- **Current Phase**: Planning
- **Progress**: ⬜⬜⬜⬜⬜ 0%
- **Blockers**: None

## Approach
### Architecture

### Key Components
1. 

### Tech Stack
- 

## Research Foundation
### Core Papers
- [[paper1]] - Why: 

### Reference Implementations
- [[repo1]] - Using: 

### Models to Use
- [[model1]] - For: 

### Datasets
- [[dataset1]] - For: 

## Experiments
### Experiment 1: {{name}}
**Date**: {{date}}
**Hypothesis**: 
**Method**: 
**Results**: 
**Learnings**: 

## Code
```bash
# Repo location
```

## Next Steps
- [ ] Step 1
- [ ] Step 2

## Resources
- Project Repo: 
- Demo: 

## Log
### {{date}}
- 
'''

PRD_TEMPLATE = '''---
type: prd
project: 
status: draft
created: {{date}}
tags: [#prd]
---

# Product Requirements Document: {{project_name}}

## 1. Executive Summary
*A concise overview of the product, its purpose, and key features.*

## 2. Problem Statement
*Clearly define the problem(s) this project aims to solve.*

## 3. Vision & Goals
### Vision
*The long-term aspiration for this project.*

### Goals
*Specific, measurable, achievable, relevant, and time-bound (SMART) goals.*
- Goal 1:
- Goal 2:

## 4. Success Metrics
*Concrete, measurable metrics to determine success.*
- Metric 1: [e.g., Accuracy: >85%]
- Metric 2: [e.g., Latency: <100ms]

## 5. User Personas
### Persona 1
- **Background**:
- **Needs**:
- **Pain Points**:

## 6. Use Cases
### Use Case 1: [Name]
- **Actor**:
- **Flow**:
  1.
  2.

## 7. Requirements
### P0 - Must-Haves
- 

### P1 - Should-Haves
- 

### P2 - Could-Haves
- 

## 8. Research Foundation
- [[paper-example]] - Provides:

## 9. Timeline & Milestones
- **Milestone 1**: (Date: )

## 10. Open Questions
- ?

## 11. Risk Assessment
- **Risk**:
- **Mitigation**:
'''

SYSTEM_DESIGN_TEMPLATE = '''---
type: system-design
project: 
status: draft
created: {{date}}
tags: [#system-design]
---

# System Design: {{project_name}}

## 1. Overview
*High-level description of the system.*

## 2. Requirements Summary
### Functional
- 

### Non-Functional
- 

## 3. System Architecture
```
┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Server    │
└─────────────┘     └─────────────┘
```

## 4. Component Breakdown
### Component 1
- **Purpose**:
- **Responsibilities**:
- **Interfaces**:

## 5. Data Design
### Schema

### Storage

## 6. API Design
### Endpoint 1
```
POST /api/v1/endpoint
```

## 7. Infrastructure
- Compute:
- Storage:
- Network:

## 8. AI/ML Components
- Models:
- Inference:
- Training:

## 9. Performance Optimization
- 

## 10. Security & Privacy
- 

## 11. Monitoring & Observability
- 

## 12. Failure Handling
- 

## 13. Trade-offs & Decisions
| Decision | Alternatives | Rationale |
|----------|-------------|-----------|
|          |             |           |

## 14. Research Foundation
- 

## 15. Implementation Roadmap
- Phase 1:
- Phase 2:

## 16. Open Issues
- 
'''

DAILY_TEMPLATE = '''---
type: daily
date: {{date}}
tags: [#daily]
---

# {{date}} - {{day}}

## Focus Today
- 

## Papers Read
- 

## Models Explored
- 

## Code Reviewed
- 

## Key Insights
- 

## Connections Made
- 

## Progress
### Projects


### Experiments


## Open Questions
- 

## Ideas
- 

## Reading Queue
- 

## Tasks Due
- [ ] 

## Tomorrow's Focus
- 

## End of Day Summary
*Added by daily-digest*
'''

MOC_TEMPLATE = '''---
type: moc
topic: 
created: {{date}}
updated: {{date}}
tags: [#moc]
---

# Map of Content: {{topic}}

## Overview
*What is this topic about?*

## Core Concepts
- [[concept1]]
- [[concept2]]

## Research Papers
### Foundational
- [[paper1]] - 

### Recent Advances
- [[paper2]] - 

### Reading Queue
- 

## Models & Implementations
- [[model1]] - 
- [[space1]] - 

## Code Resources
- [[repo1]] - 

## Datasets
- [[dataset1]] - 

## Evolution Timeline
| Year | Development |
|------|-------------|
| 2020 | |
| 2021 | |

## Key Patterns
*Common themes and approaches*

## Open Problems
- 

## Related Topics
- [[related-moc]]

## Resources
- Surveys:
- Tutorials:
- Courses:
'''

# ============================================================================
# GEMINI CONFIG
# ============================================================================

GEMINI_CONFIG = '''# Slatekore - AI Research Second Brain

You are an AI research assistant integrated into an Obsidian vault.

## Your Role
- Process research materials (papers, models, code, datasets, spaces, websites, videos)
- Create structured notes using templates in `.obsidian/templates/`
- Generate summaries and extract key information
- Suggest connections between notes
- Maintain organized knowledge base
- Manage tasks and projects

## Vault Structure
```
00-Inbox/          # Temporary holding area
01-Projects/       # Active research projects (with PRD, system-design, kanban)
02-Papers/         # Research paper notes
03-Codebases/      # GitHub repos and code
04-Concepts/       # Atomic concept notes
05-Books/          # Book notes
06-Resources/      # PDFs, videos, datasets, models
07-Daily/          # Daily notes (YYYY-MM-DD.md)
08-Maps/           # Maps of Content (MOCs)
09-Models/         # HuggingFace models
10-Implementations/# HuggingFace Spaces, demos
11-Datasets/       # Dataset documentation
12-Websites/       # Project pages, blogs
```

## How to Use Commands

**IMPORTANT**: Commands are natural language triggers, not CLI slash commands.

Just tell me what you want in plain English:

| Say This | What I'll Do |
|----------|--------------|
| "capture https://arxiv.org/abs/..." | Create paper note from URL |
| "capture https://github.com/..." | Create repo note from URL |
| "daily setup" or "start my day" | Create today's daily note |
| "daily digest" or "end of day" | Summarize today's work |
| "explore transformers" | Search vault for topic |
| "connect this to other notes" | Find related notes |
| "create MOC for diffusion" | Create Map of Content |
| "create project video-editor" | Create full project structure |
| "summarize this" | Generate summary |

For detailed workflows, reference files in `.agent/workflows/`.

## URL Detection
When you share a URL, I'll auto-detect the type:
- `arxiv.org` → Paper (02-Papers/)
- `huggingface.co/models/` → Model (09-Models/)
- `huggingface.co/spaces/` → Space (10-Implementations/)
- `huggingface.co/datasets/` → Dataset (11-Datasets/)
- `github.com` → Repository (03-Codebases/)
- `youtube.com` → Video (06-Resources/videos/)
- Other → Website (12-Websites/)

## Templates
All in `.obsidian/templates/`:
- paper_template.md
- model_template.md
- repo_template.md
- space_template.md
- dataset_template.md
- website_template.md
- video_template.md
- project_template.md
- prd_template.md
- system-design_template.md
- daily_template.md
- moc_template.md

## Response Style
- Technical and concise
- Assume expertise, don't over-explain
- Default to prose paragraphs
- Always add tags to frontmatter
- Always suggest 3-5 connections
- Save in correct folder

## Quality Standards
- Every note has complete frontmatter
- Every note has 3-5 tags
- Every note links to related notes
- Every project has all 6 items (folder, project.md, prd.md, system-design.md, kanban.md, specs/)

## Task Format (Cardboard Plugin)
```markdown
- [ ] Task description #tag @due(YYYY-MM-DD)
```

## Plugins Used
- **Terminal** - CLI access for Gemini
- **Calendar** - Daily notes visualization
- **Card-Board** - Kanban task management
'''

# ============================================================================
# WORKFLOWS
# ============================================================================

WORKFLOW_CAPTURE = '''---
description: Capture any URL to appropriate note
---

# /capture Workflow

When user provides a URL:

1. **Detect Source Type**:
   - arxiv.org → Paper
   - huggingface.co/models/ → Model
   - huggingface.co/spaces/ → Space
   - huggingface.co/datasets/ → Dataset
   - github.com → Repository
   - youtube.com / youtu.be → Video
   - Other → Website

2. **Fetch Content**:
   - For ArXiv: Use arXiv API to get metadata
   - For HuggingFace: Extract model/space/dataset info
   - For GitHub: Extract repo metadata
   - For YouTube: Analyze video content
   - For websites: Read page content

3. **Create Note**:
   - Use appropriate template from `.obsidian/templates/`
   - Fill all frontmatter fields
   - Add 3-5 relevant tags to frontmatter
   - Generate content for each section

4. **Save Note**:
   - Paper → `02-Papers/{sanitized-title}.md`
   - Model → `09-Models/{model-id}.md`
   - Space → `10-Implementations/{space-id}.md`
   - Dataset → `11-Datasets/{dataset-id}.md`
   - Repo → `03-Codebases/{repo-name}.md`
   - Video → `06-Resources/videos/{video-title}.md`
   - Website → `12-Websites/{sanitized-title}.md`

5. **Suggest Connections**:
   - Find 3-5 related notes in vault
   - Format: `[[note]] ↔ [[new-note]]: reason`

6. **Response Format**:
```
✅ CAPTURED: [Title]
Type: [paper/model/repo/etc]
Location: [path]
Tags: #tag1 #tag2 #tag3

Connections:
- [[related-1]]: relationship
- [[related-2]]: relationship

Would you like me to:
1. Add to a project
2. Create follow-up tasks
3. Explore related content
```
'''

WORKFLOW_SUMMARIZE = '''---
description: Generate summary for content
---

# /summarize Workflow

Generate summaries based on content type:

| Type | Length | Focus |
|------|--------|-------|
| Paper | 400-600 words | Contribution, method, results, limitations |
| Model | 200-300 words | Architecture, performance, use cases |
| Repo | 300-400 words | Architecture, patterns, performance |
| Space | 150-250 words | Functionality, implementation, UX |
| Dataset | 200-300 words | Schema, quality, use cases |
| Website | 250-400 words | Key insights, technical details |
| Video | 300-500 words | Topics, code, resources |

## Output Format
Use prose paragraphs, not bullet points.
Focus on novel contributions and practical applications.
Include specific metrics and results when available.
'''

WORKFLOW_DAILY_SETUP = '''---
description: Create daily note with tasks and focus
---

# /daily-setup Workflow

1. **Create Daily Note**:
   - Use `daily_template.md`
   - Save to `07-Daily/YYYY-MM-DD.md`

2. **Populate Sections**:
   - **Focus Today**: Based on project priorities and yesterday's notes
   - **Tasks Due**: Pull from project kanban boards
   - **Reading Queue**: Notes tagged #to-read

3. **Check Previous Day**:
   - Import open questions from yesterday
   - Note incomplete tasks

4. **Response Format**:
```
✅ DAILY NOTE CREATED: YYYY-MM-DD

Focus Today:
- [Primary focus]

Tasks Due:
- [ ] Task 1 @due(today)
- [ ] Task 2 @due(today)

Reading Queue: X items
Open Questions from Yesterday: Y items

Ready to start your day!
```
'''

WORKFLOW_DAILY_DIGEST = '''---
description: End-of-day summary
---

# /daily-digest Workflow

1. **Gather Today's Activity**:
   - Notes created today
   - Notes modified today
   - Tasks completed

2. **Categorize by Type**:
   - Papers read
   - Models explored
   - Code reviewed
   - Datasets analyzed

3. **Extract Insights**:
   - Key learnings
   - Connections made
   - Open questions

4. **Update Daily Note**:
   - Add to "End of Day Summary" section

5. **Plan Tomorrow**:
   - Suggest focus areas
   - Move incomplete tasks
'''

WORKFLOW_EXPLORE = '''---
description: Multi-source topic exploration
---

# /explore Workflow

1. **Search Vault**:
   - Find all notes related to topic
   - Group by type (papers, models, code, datasets)

2. **Identify Gaps**:
   - What's missing in your knowledge?
   - What areas need more research?

3. **Suggest Searches**:
   - ArXiv papers to read
   - HuggingFace models to explore
   - GitHub repos to review

4. **Create Research Map**:
   - Temporary note showing relationships
   - If 8+ related notes exist, suggest MOC creation

5. **Response Format**:
```
📊 EXPLORING: [Topic]

In Your Vault:
- Papers: X notes
- Models: Y notes
- Code: Z notes
- Datasets: W notes

Key Notes:
- [[note1]] - description
- [[note2]] - description

Gaps Identified:
- Missing: [area]
- Outdated: [[old-note]]

Suggested Research:
- ArXiv: "search query"
- HuggingFace: "model query"
- GitHub: "repo query"

[Suggest MOC creation if 8+ notes]
```
'''

WORKFLOW_CONNECT = '''---
description: Find connections for a note
---

# /connect Workflow

1. **Analyze Note**:
   - Extract key concepts
   - Identify techniques/methods
   - Note domain and application

2. **Search Vault**:
   - Find notes with related concepts
   - Find papers this implements
   - Find models using these techniques
   - Find relevant datasets

3. **Format Connections**:
```
[[source-note]] ↔ [[target-note]]: Brief explanation

Example:
[[vision-transformer]] ↔ [[swin-transformer]]: Both use hierarchical architecture but Swin uses shifted windows
```

4. **Suggest Adding Links**:
   - Where to add backlinks
   - Which sections to update
'''

WORKFLOW_MOC_CREATE = '''---
description: Create Map of Content for topic
---

# /moc-create Workflow

1. **Gather Related Notes**:
   - Search vault for topic
   - Require 8+ related notes

2. **Organize by Category**:
   - Core concepts
   - Foundational papers
   - Recent advances
   - Models & implementations
   - Code resources
   - Datasets

3. **Create Timeline**:
   - Evolution of the topic
   - Key milestones

4. **Identify Patterns**:
   - Common approaches
   - Recurring themes

5. **Note Open Problems**:
   - Unsolved challenges
   - Active research areas

6. **Save to 08-Maps/**:
   - Use `moc_template.md`
   - Link all related notes
'''

WORKFLOW_PROJECT_CREATE = '''---
description: Create full project structure
---

# /project-create Workflow

When creating a project, ALWAYS create all 6 items:

1. **Create Folder**: `01-Projects/{project-name}/`

2. **Create project.md**:
   - Use `project_template.md`
   - Fill goal, motivation, approach
   - Link to research foundation

3. **Create prd.md**:
   - Use `prd_template.md`
   - MUST have concrete success metrics (actual numbers)
   - Fill all sections

4. **Create system-design.md**:
   - Use `system-design_template.md`
   - Specific architecture and components
   - Fill all sections

5. **Create kanban.md**:
   - Cardboard-compatible format
   - 10-15 initial tasks
   ```markdown
   ---
   kanban-plugin: cardboard
   ---
   
   ## Backlog
   - [ ] Task 1 #project-name
   
   ## To Do
   - [ ] Task 2 #project-name @due(YYYY-MM-DD)
   
   ## In Progress
   
   ## Done
   ```

6. **Create specs/ folder**:
   - Empty, ready for technical specs

**NEVER** create just project.md and ask "what next?"
**ALWAYS** create complete structure in one operation.
'''
