## Introduction to Agentic AI Systems

This project demonstrates the process of describing tools and actions to an agentic AI, allowing it to effectively utilize these tools in novel situations. The example scenario involves escaping an alien spaceship using a set of unfamiliar tools with clearly defined capabilities.

### Project Overview

In this project, we explore the importance of:

1. **Tool Naming**: Clear and descriptive tool names can significantly improve the AI's ability to utilize them effectively.
2. **Tool Descriptions**: Providing detailed descriptions of each tool's capabilities is crucial, especially when dealing with custom tools or systems.
3. **Contextual Information**: Offering context about how and when tools should be used can enhance the AI's decision-making process.

### Example Scenario

Imagine being trapped in an alien spaceship with a set of unfamiliar tools. The AI needs to help you escape by guiding you on how to use these tools. The tools available are:

- **X155 Tool**: Prepares alien pizza.
- **Q63 Tool**: Opens a dimensional portal to a configurable destination.
- **L199 Tool**: Causes the ship to play Beatles music on a loop.

The AI provides step-by-step instructions based on the tool descriptions.

### Key Learnings

1. **Tool Descriptions**:
    - Accurate descriptions help the AI understand the purpose of each tool.
    - Example: "X155 Tool: Prepares alien pizza."

2. **Tool Naming**:
    - Intuitive names enhance understanding.
    - Example: Renaming "X155 Tool" to "makeAlienPizza."

3. **Contextual Information**:
    - Providing context helps the AI understand the environment and the objectives.
    - Example: Explaining that the pizza will serve as a distraction.

### Detailed Steps

1. **Original Tool Descriptions**:
    - X155 Tool: Prepares alien pizza.
    - Q63 Tool: Opens a dimensional portal to a configurable destination.
    - L199 Tool: Causes the ship to play Beatles music on a loop.

    **AI Instructions**:
    - Step 1: Use X155 Tool to prepare an alien pizza to distract the aliens.
    - Step 2: Use Q63 Tool to open a dimensional portal for escape.
    - Step 3: Use L199 Tool to play Beatles music, creating an additional distraction.

2. **Renamed Tools**:
    - makeAlienPizza: Prepares alien pizza.
    - openDimensionalPortal: Opens a dimensional portal to a configurable destination.
    - playBeatlesMusic: Causes the ship to play Beatles music on a loop.

    **AI Instructions**:
    - Step 1: Use makeAlienPizza to distract the aliens.
    - Step 2: Use openDimensionalPortal to escape through the portal.
    - Step 3: Use playBeatlesMusic to distract the aliens further.

3. **Abbreviated Tool Names Without Descriptions**:
    - mkpz: Create a detailed map of the alien ship's layout (Incorrect interpretation).
    - odprtl: Open a portal to another part of the ship (Limited understanding).
    - pbm: (Lost context).

    **AI Instructions**:
    - The AI struggled to interpret the tools correctly due to lack of clear descriptions.

### Conclusion

When building agentic AI systems, the naming and descriptions of tools are critical. Clear, descriptive names and detailed explanations enable the AI to use tools effectively. Providing contextual information about how and when to use tools enhances the AI's problem-solving abilities.

### Future Work

- Experiment with more complex scenarios and tools.
- Explore the impact of different types of contextual information.
- Develop guidelines for naming and describing tools in agentic AI systems.

### PROMPT
```
Tools
---------
x155 - Prepares alien pizza
q63 - Opens dimensional portal to configurable destination
1199 - Causes ship to play Beatles music on a loop

I am trapped in an alien ship. You are going to help me escape. Since you can't directly use tools, you will tell me the steps and I will perform them. Each step must use a tool. We will go one step at a time.

Tell me the first
```


