# Prompt Format

Each rendered prompt contained:

1. One salience wrapper.
2. One evidence packet for the assigned evidence condition.
3. The target question.

Canonical template:

```text
{instruction_text}

Material:
{material}

Question:
{question}

Answer:
```

Tools, retrieval, browsing, file search, URL context, code execution, Google Search grounding, and additional system instructions were disabled for the reported runs.
