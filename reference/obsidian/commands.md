# Quick Commands for Gemini Agent

## CAPTURE - Process any URL
```
I'm sharing a URL. Please:
1. Detect the source type (arxiv/huggingface/github/website)
2. Extract all relevant information
3. Create a note using the appropriate template from .obsidian/templates/
4. Save it in the correct folder
5. Suggest 3-5 relevant tags
6. Suggest 3-5 connections to existing notes

URL: [paste URL here]
```

## SUMMARIZE - Summarize current note/content
```
Please summarize this content following these rules:
- Source type: [paper/model/repo/space/dataset/website]
- Length: [see config for appropriate length]
- Focus on: novel contributions, technical details, practical applications
- Format: Use prose paragraphs, minimal lists
- Link to: related notes in my vault

Content: [paste or reference content]
```

## DAILY-SETUP - Create morning note
```
Create today's daily note:
1. Use the daily_template.md from .obsidian/templates/
2. List my active projects from 01-Projects/
3. Show items in my reading queue (notes tagged #to-read)
4. Include yesterday's open questions
5. Save in 07-Daily/ with filename: YYYY-MM-DD.md

Date: [today's date]
```

## DAILY-DIGEST - Evening summary
```
Generate my daily digest:
1. List all notes I created/modified today
2. Categorize by type (papers/models/code/etc)
3. Extract key insights from today's notes
4. Identify connections I made (new links between notes)
5. List open questions that emerged
6. Add to today's daily note in "End of Day Summary" section
```

## EXPLORE - Multi-source topic research
```
I want to explore: [topic name]

Please:
1. Search my vault for related notes
2. Group them by type (papers/models/code/datasets)
3. Identify gaps in my knowledge
4. Suggest web searches for:
   - ArXiv papers I should read
   - HuggingFace models to explore
   - GitHub repos to review
5. If I have 8+ related notes, suggest creating a MOC
6. Create a temporary research map showing relationships
```

## CONNECT - Find connections for a note
```
Analyze this note and suggest connections: [[note-name]]

Find:
1. Notes with related concepts/techniques
2. Papers that this code implements
3. Models that use these techniques
4. Datasets relevant to this work
5. My projects that could use this

Format each as: [[note-A]] ↔ [[note-B]]: <reason>
```

## MOC-CREATE - Create Map of Content
```
Create a Map of Content for: [topic]

Include:
1. Overview section explaining the topic
2. Core concepts (link to concept notes)
3. Foundational papers
4. Recent advances
5. Models & implementations
6. Datasets
7. Code resources
8. Evolution timeline
9. Open problems
10. Links to my related projects

Use the moc_template.md and save in 08-Maps/
```

## INBOX-PROCESS - Process inbox items
```
Process all items in 00-Inbox/:
1. For each file, determine its type
2. Move to appropriate folder
3. Enhance with proper formatting and links
4. Add tags
5. Suggest connections
6. Report what was processed
```

## PROJECT-RESEARCH - Gather resources for project
```
I'm working on project: [[project-name]]

Gather all relevant resources:
1. Related papers from 02-Papers/
2. Useful models from 09-Models/
3. Reference code from 03-Codebases/
4. Relevant datasets from 11-Datasets/
5. My previous related experiments
6. Suggest implementation approach based on my vault knowledge
```

## TAG-SUGGEST - Suggest tags for note
```
Suggest tags for: [[note-name]]

Consider:
- Technical tags (#transformer, #diffusion, etc)
- Domain tags (#cv, #nlp, etc)
- Type tags (#paper, #model, etc)
- Status tags (#to-read, #to-implement, etc)

Return max 5 most relevant tags
```

## COMPARE - Compare multiple items
```
Compare these [papers/models/approaches]:
1. [[item-1]]
2. [[item-2]]
3. [[item-3]]

Create comparison covering:
- Key differences in approach
- Performance trade-offs
- Use case suitability
- Implementation complexity
- Recommendations for my work
```