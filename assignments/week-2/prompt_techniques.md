**Prompt Techniques**

Gyan Kannur

DSC 670

**Problem #2: Sentiment Analysis**

_Type:_ Sentiment Analysis

_Input:_ That was FINE example of teaching an intelligent automation class. :-/

_Output:_ The emotions the text conveys.

_Note._ Upon searching, the emoticon :-/ represents a skeptical, uncertain, or hesitant facial expression, often conveying mixed emotions, mild displeasure, disappointment, or awkwardness.

**Analysis**

This problem addresses sentiment analysis, specifically a sentence paired with an emoticon. The statement _"That was FINE example... :-/"_ can be divided into two analytical components: primary and secondary emotions.

**Primary Emotions**

Primary emotions are the first, automatic reactions to a situation. They are often instinctive, universal, and brief. In the context of this prompt engineering problem:

- _Stimulus:_ A class that was perhaps poorly taught or frustrating.
- _Primary Emotion:_ Likely disappointment or frustration - the core feeling that arose immediately after the experience.
- _Common Examples:_ Joy, sadness, fear, anger, surprise, and disgust.

**Secondary Emotions**

Secondary emotions are the emotional reactions to the primary emotion. They are often more complex, learned, and can act as a mask for the original feeling, shaped by thoughts, social expectations, or defense mechanisms.

- _Expression:_ "That was FINE example... :-/"
- _Secondary Emotion:_ Sarcasm or cynicism. Rather than stating "I am disappointed," the user employs irony to distance themselves from the vulnerability of being upset.
- _Relevance to AI:_ A large language model (LLM) that identifies only "positive" (due to the word "fine") or "negative" misses the secondary layer of sarcasm, which represents the most critical dimension of the communication.

**Prompt Technique**

To ensure the LLM captures underlying subtext rather than literal definitions, the following strategy is proposed.

_Strategy:_ Few-Shot Prompting with Emotional Mapping

_Prompt:_ You are a linguistics expert specializing in digital communication. Analyze the following inputs and identify the primary and secondary emotions conveyed, paying close attention to capitalization and emoticons.

_Input:_ "I am so much relieved that we could finally make it :)" _Output:_ Primary: Kindness; Secondary: Relief

_Input:_ "Did I have a good time? Definitely :/" _Output:_ Primary: Thoughtful; Secondary: Sarcasm

_Input:_ "That was FINE example of teaching an intelligent automation class. :-/" _Output:_ Primary: Sarcasm; Secondary: Disapproval

**Problem #3: Simple Math**

_Type:_ Text Generation and Reasoning

_Output:_ The sum of 2,292.32 and 4,494 1/3

_Rules:_ Return only the result expressed as a fraction.

**Prompt Technique**

The objective is to ensure that an LLM correctly processes different numerical types - a decimal and mixed numbers and performs addition without losing precision through floating-point approximations. The following prompt utilizes a specialized technique to achieve the required fractional output.

_Prompt 1: Chain-of-Thought Reasoning_

Perform the following calculation by following each step exactly:

- Convert the decimal 2,292.32 into its simplest fractional form.
- Convert the mixed number 4,494 1/3 into an improper fraction.
- Add the fractions together to find the final sum.
- Provide only the final result as a single improper fraction.

**Inference**

In this strategy, chain-of-thought (CoT) reasoning serves as a logic gate. By requiring the conversion of 2,292.32 to 57,308/25 and 4,494 1/3 to 13,483/3, the model establishes a precise symbolic baseline. The subsequent steps of adding the fractions and returning the result ensure the desired outcome is achieved.

**Conclusion:**

Effecting outcomes can be achieved by inducing the right prompting techniques which ensures LLMs perform complex tasks. Few prompt techniques discussed like Few-shot and chain-of-thought strategies, the model accurately bridges the gap between literal text and nauanced human sentiment or precise maths constants. These methods successfully mitigate common AI errors such as the misinterpretation of sarcasm and the rounding of repeating decimals