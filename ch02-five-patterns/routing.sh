#!/bin/bash
# Multi-Agent Development with Claude Code -- Chapter 2
# Routing: select the model based on task classification
TASK_TYPE=$(claude -p "Classify the following task as one of: \
  simple question / code change / architecture design \
  Task: $USER_QUERY" \
  --output-format json | jq -r '.classification')

case $TASK_TYPE in
  "simple question")
    # Lightweight model for fast responses
    claude -p "$USER_QUERY" --model haiku
    ;;
  "code change")
    # Standard model for implementation
    claude -p "$USER_QUERY" --model sonnet
    ;;
  "architecture design")
    # Top-tier model for deep analysis
    claude -p "$USER_QUERY" --model opus
    ;;
esac
