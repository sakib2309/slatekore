# Common Workflows

## Morning Routine
1. Open terminal in Obsidian
2. Run: DAILY-SETUP command
3. Review reading queue
4. Pick focus for the day

## When You Find a Paper
1. Copy ArXiv URL
2. Terminal: CAPTURE command with URL
3. Agent creates note in 02-Papers/
4. Review and add personal insights
5. Optional: CONNECT to find related notes

## When You Find a Model
1. Copy HuggingFace model URL
2. Terminal: CAPTURE command  
3. Agent creates note in 09-Models/
4. If relevant to project: link to project note
5. Optional: compare with similar models

## When Exploring a New Topic
1. Terminal: EXPLORE command with topic
2. Review what you already have
3. Follow suggested searches
4. Capture new findings
5. If enough coverage: Create MOC

## When Starting a Project
1. Create project note using template
2. Terminal: PROJECT-RESEARCH command
3. Review all gathered resources
4. Link relevant papers/models/code
5. Document approach and experiments

## Evening Routine
1. Terminal: DAILY-DIGEST command
2. Review what you learned
3. Process inbox if needed
4. Note tomorrow's focus

## Weekly Review
1. Review 07-Daily/ notes from the week
2. Identify patterns in your learning
3. Create/update MOCs for topics with enough coverage
4. Archive completed projects
5. Update active project status

## Pro Tips for Gemini Agent

1. **Be Specific**: Always tell the agent which template to use and where to save

2. **Review and Enhance**: The agent creates structure, you add insights and personal context

3. **Build Progressively**: Start with simple captures, evolve to complex MOCs

4. **Link Explicitly**: Ask agent to link new notes to existing ones by name

5. **Iterate**: If a note isn't formatted right, ask agent to fix it referencing the template

6. **Use Natural Language**: No need for rigid commands, explain what you want

7. **Provide Context**: Remind agent of your role and focus when needed

8. **Save Good Prompts**: Keep effective prompts in .obsidian/commands.md for reuse

9. **Weekly Review**: Have agent analyze patterns in your learning to suggest focus areas

10. **Evolve Templates**: As you use the system, refine templates and update agent instructions

---

## Troubleshooting

**Agent not following template?**
→ Explicitly reference the template file: "Use paper_template.md from .obsidian/templates/"

**Links not being created?**
→ Ask agent to "suggest connections" as a separate step after creation

**Summaries too generic?**
→ Specify: "Generate a 500-word technical summary focusing on [specific aspects]"

**Can't find notes?**
→ Ask agent: "Search my vault for notes about [topic]"

**Agent forgot instructions?**
→ Say: "Please re-read .obsidian/agent-prompt.md and continue"
