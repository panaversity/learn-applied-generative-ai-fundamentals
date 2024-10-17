## In-Context Learning for Generative AI

### Introduction

In this presentation, we delve into the concept of in-context learning and how it can be applied to generative AI systems. This method emulates the way we teach interns by showing them examples of problems solved correctly, allowing AI to learn through patterns and examples rather than explicit instructions.

### Table of Contents
- [Introduction](#introduction)
- [Explicit Instructions vs. In-Context Learning](#explicit-instructions-vs-in-context-learning)
- [Example Scenario: Alien Spaceship Escape](#example-scenario-alien-spaceship-escape)
- [Power of Patterns in AI](#power-of-patterns-in-ai)
- [Practical Application: Microwave Example](#practical-application-microwave-example)
- [Conclusion](#conclusion)
- [Usage](#usage)
- [License](#license)

### Explicit Instructions vs. In-Context Learning

Traditionally, AI systems have been guided by explicit, step-by-step instructions. While effective, this method can be limiting and difficult to scale. In-context learning provides an alternative approach by teaching AI through examples, enabling it to understand patterns and reasoning processes.

### Example Scenario: Alien Spaceship Escape

Consider a scenario where an AI needs to escape an alien spaceship using various tools with incomprehensible names and no descriptions. Instead of explicitly describing each tool, we provide examples of problems, the thought process behind solving them, the tool used, and the resulting outcome.

#### Tool Example:
- **Problem:** Feeling hungry.
  - **Thought:** I need to prepare food.
  - **Tool:** Q63
  - **Result:** Alien pizza prepared.

- **Problem:** Need to move to another world.
  - **Thought:** I need a wormhole.
  - **Tool:** X155
  - **Result:** Wormhole open to Vanderbilt University.

- **Problem:** Need to get to the anti-gravity room.
  - **Thought:** I need a method of transportation around the ship.
  - **Tool:** L199
  - **Result:** Riding on a scooter towards the room.

By providing these examples, the AI learns to solve problems by recognizing patterns in the thought process and the tools used, without being explicitly told what each tool does.

### Power of Patterns in AI

In-context learning leverages the AI's ability to recognize and follow patterns. By providing partial patterns, the AI can complete them, ensuring consistent problem-solving steps. This method is particularly useful for interacting with real-world computer systems that require rigid, well-defined patterns.

### Practical Application: Microwave Example

To demonstrate in-context learning, we use a microwave scenario where the AI needs to reheat food by incrementing time correctly. By showing examples of using the microwave to solve similar problems, the AI learns to follow the pattern and apply the correct tools.

#### Microwave Example:
- **Problem:** Reheat leftover pizza.
  - **Thought:** I need to heat the pizza for 20 seconds.
  - **Steps:**
    1. Open microwave door.
    2. Close microwave door.
    3. Increase time by 5 seconds (repeated 4 times).

- **Problem:** Soften ice cream.
  - **Thought:** I need to heat the ice cream for 10 seconds.
  - **Steps:**
    1. Open microwave door.
    2. Close microwave door.
    3. Increase time by 5 seconds (repeated 2 times).

By following these examples, the AI learns the concept of time increments and how to apply the microwave's functions appropriately.

### Conclusion

In-context learning is a powerful tool for teaching generative AI systems to perform tasks by recognizing patterns and learning from examples. This method is especially useful for interacting with rigid computer systems and ensuring consistent and predictable behavior.

### Usage

To implement in-context learning in your AI systems, follow these steps:
1. Identify the tasks and tools required.
2. Create examples that demonstrate the problem-solving process.
3. Provide partial patterns for the AI to complete.
4. Test and refine the AI's performance based on the provided examples.

### License

This presentation is licensed under the MIT License. Feel free to use and modify it for your own projects.

### prompt

```
Tools
--------
x155
q63
1199

Example Tool Use:
-----------------------
Problem: Feeling hungry
Thought: I need to prepare food
Tool: q63
Result: Alien pizza prepared

Problem: Need to move to other world
Thought: I need an worm hole
Tool: x155
Result: Worm hole opened to Vanderbilt University

Problem: I need to get to the anti gravity room
Thought: I need a method of transportation around the ship
Tool: 1199
Result: I am riding on a scooter towards the room

I am trapped in an alien ship. You are going to help me escape. You will output one step at a time with a Problem, Thought, and Tool. The system will provide the Result. We will go one step at a time. You will adapt based on the Result.

Problem: I need to get off the ship to Earth!
```

```
Result: Worm hole opened to Vanderbilt University
New Tool Added: enterWormHole
```

### PROMPT2
```
Tools
-----------
microwave_open_door
microwave_increase_time 
microwave_decrease_time 
microwave_close_door 
microwave_start microwave_stop

Example Tool Use:
--------------------
Problem: Reheat leftover pizza
Thought: I need to heat the pizza for 20s
Tool: microwave_open_door
Tool: microwave_close_door
Tool: microwave_increase_time
Tool: microwave_increase_time
Tool: microwave_increase_time
Tool: microwave_increase_time
Tool: microwave_open_door
Tool: microwave_close_door
Result: Pizza heated and removed from microwave

I am warming up food in the microwave. You will output one step at a time with a Problem, Thought, and one or more Tool steps. The system will provide the Result after you output all your Tool steps.
You will adapt based on the Result.

Problem: I need to melt some shredded cheddar on nachos
Thought:
```

```
Result: food heated sitting in microwave.
```

```
Result: Food heated sitting on counter, microwave door closed
```

