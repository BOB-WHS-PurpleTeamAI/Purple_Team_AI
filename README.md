# Purple_Team_AI
- This project, Purple_Team_AI, is focused on developing an innovative cybersecurity solution by integrating advanced techniques from Red Team, Blue Team, and Purple Team methodologies.
- An SOAR solution that can block known vulnerabilities and zero-day attacks through attacks and defenses between the RL-based automated penetration test Red Team (Fuzzing, AEG) and the automated patch system Blue Team
The goal is to implement an automation MVP model that automates the generation of exploit codes for vulnerabilities that were discovered during the project. 
Target not determined
ex) 
1. Automatic Fuzzing Test-based : windows programs etc..
2. Web application-based
3. Sysyem network-based

# Red Team <-- WhiteHatSchool Project 
- The Red Team leverages expertise in AEG (Automatci Exploit Generation) techniques and reinforcement learning algorithms such as A3C and Q-learning. Automated penetration testing, driven by meta-exploits, prioritizes successful penetrations via vulnerabilities. The model is trained with a weighted emphasis on successful penetration based on vulnerabilities.
1. binary code-based Automatic Exploit Generation(AEG)
2. A3C, Q-learning etc.. RL agorithms Status, Environment(OpenAI) build
	 - Status : network information through network scanning
	 - Weighing : Vnlnerability Found
3. Make automatic Analysis Report
4. Automatic Penetration simulation <-- Matasploit
5. Make PlayBook 

# Blue Team
- The Blue Team receives outputs from Red Team AI, including explored vulnerabilities and corresponding exploit codes. They implement automated patches and build secure systems, ensuring vulnerabilities are effectively mitigated.
1. Vulnerability-based automated patching discovered
2. SOAR Solution
3. Report on the Web 

# Purple Team
- The Purple Team focuses on the collaborative synergy between Red Team AI and Blue Team AI's MVPs. The goal is to derive an AI-based next-generation Security Orchestration, Automation, and Response (SOAR) solution when both Red Team and Blue Team MVPs are implemented.

# MVP Model
- The MVP Model aims to construct a minimal functional prototype within a specific domain (e.g., web, Windows PowerShell). This prototype demonstrates the core capabilities of the Purple Team AI solution.

# What Should We Do
- Implement technical frameworks required for Red Team and Blue Team functionalities.
Develop algorithms and automation processes essential for Red Team's penetration testing and Blue Team's automated patching.
- Setting a Targeting
1. Automatic Fuzzing Test-based : windows programs
2. Web application-based
3. Sysyem network-based

# Start-Up
- At this stage, the project's start-up involves defining the project scope, outlining team roles, and planning the initial technical implementation. The team will focus on setting clear goals, determining technological requirements, and establishing the foundational framework for the Purple Team AI project.
