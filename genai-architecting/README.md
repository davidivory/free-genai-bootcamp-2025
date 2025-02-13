## Overview

This project aims to enhance the language learning experience at a Thai Language Learning School by integrating AI-driven learning applications. The primary goal is to leverage open-source and free resources to provide scalable, cost-effective, and privacy-conscious language learning tools that can eventually expand to assist underprivileged areas worldwide.



## Functional Requirements

Infrastructure Ownership: The client prefers to own and manage their infrastructure to maintain privacy and reduce long-term costs.

Budget Constraints: Investment in an AI PC with a budget of $10,000 - $15,000.

User Base: The system must support 300 active students located in Bangkok, Thailand.

Learning Applications:

- - Writing Practicing App

- - Text Adventure Immersion Game

- - Light Visual Novel Immersion

- - Reading Module

- - Sentence Constructor (AI-assisted)

- - Visual Flashcard Vocab

- - Speak to Learn

## Assumptions

The entire infrastructure will be open-source and self-hosted on a powerful on-prem machine.

The bandwidth and computing power will be sufficient for 300 concurrent users.

The learning record store will integrate with AI-driven applications.

## Data Strategy

Copyright Compliance: Licensed materials will be purchased, and original content will be developed to reduce licensing costs.

Data Storage: A structured database will store learning materials, student progress, and AI-generated content.

Data Privacy: No sensitive personal data will be shared externally; all processing will be conducted on-prem.

Knowledge Base: AI will be trained on curated language datasets to improve contextual understanding and sentence construction.

## Model Selection and Development

Hosting Strategy: The model will be self-hosted to avoid dependency on SaaS providers.

Model Type: A lightweight 7B parameter LLM with RAG (Retrieval-Augmented Generation) for contextual responses.

Input-Output Modality: Primarily text-to-text with structured sentence recommendations.

Optimization:

- - Guardrails for filtering inappropriate responses.

- - Prompt caching for efficiency.

- - Fine-tuning if necessary for Thai language fluency.

## Infrastructure Design

On-Prem Deployment: A high-performance AI workstation with GPU acceleration.

Modular Architecture: Designed for future expansion to multiple languages.

Hybrid Considerations: Potential integration with cloud resources for backup or additional processing power.

## Integration and Deployment

APIs: AI services will be exposed through RESTful APIs for easy integration with existing systems.

CI/CD Pipelines: Automated model deployment, updates, and monitoring.

Compatibility: Ensuring smooth integration with legacy learning management systems.

## Monitoring and Optimization

Performance Metrics: Regular tracking of AI response times and user engagement.

Feedback Loop: User input will refine AI-generated responses.

Cost Monitoring: Alerts for compute usage to maintain budget efficiency.

## Governance and Security

Responsible AI Use: Guardrails for bias detection, content moderation, and ethical AI practices.

Access Control: Role-based access for teachers and students.

Regulatory Compliance: Adherence to data protection laws in Thailand.

Scalability and Future-Proofing

Containerization: Using Docker/Kubernetes for portability and scaling.

Model Versioning: Tracking updates and fine-tuned models.

Expanding Reach: Future plans to adapt the platform for other underprivileged regions worldwide.

## Business Considerations

Cost Transparency:

AI server hardware costs.

AI model storage and processing costs.

Vendor Lock-in Avoidance:

- - Preference for open-source solutions.

IBM Granite will be considered as it is open source and self deployable
There are 77 models so we will need to decide which ones to implement and how to do it correctly

https://huggingface.co/ibm-granite

## Guardrails Implementation

Input Guardrails: Pre-processing user queries to filter inappropriate input.

Output Guardrails: Ensuring AI-generated responses are safe and appropriate.

Sandboxing: Running AI models in isolated environments to prevent unintended behaviors.

## Conclusion

This AI-driven language learning system is designed to provide an interactive and scalable solution for language education. By leveraging open-source tools, self-hosted infrastructure, and modular architecture, we ensure a cost-effective, private, and adaptable platform that can be expanded globally, particularly to underserved communities.