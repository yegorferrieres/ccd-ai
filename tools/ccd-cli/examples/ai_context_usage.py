#!/usr/bin/env python3
"""
Example usage of AI-CONTEXT commands in CCD CLI

This example demonstrates how to use the new AI-CONTEXT integration commands.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and display the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print('='*60)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("✅ Success!")
        if result.stdout:
            print("Output:")
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print("Error output:")
            print(e.stderr)
        return False
    return True

def main():
    """Main example function."""
    print("🚀 CCD CLI AI-CONTEXT Integration Examples")
    print("This example demonstrates the new AI-CONTEXT commands.")
    
    # Example 1: Add AI-CONTEXT comments to a source file
    print("\n📝 Example 1: Adding AI-CONTEXT comments")
    print("This will add AI-CONTEXT comments to a Go source file.")
    
    # Create a sample context file first
    context_content = """---
file_path: "examples/sample.go"
language: "go"
domain: "backend"
size: "medium"
lines: 45
updated_at: "2025-08-28T10:00:00Z"
dependencies: ["router.go", "middleware.go", "config.go"]
tags: ["entry-point", "server", "initialization"]
owner: "backend-team"
next_review: "2025-09-27"
status: "active"
---

## Overview
Main entry point for the Edge Gateway service.

## Purpose
This service acts as the primary entry point for all external API requests,
providing authentication, rate limiting, and request routing.

## Dependencies
- router.go: Handles HTTP routing
- middleware.go: Provides authentication and logging
- config.go: Manages service configuration

## Key Components
- Server initialization
- Middleware setup
- Route configuration
- Graceful shutdown
"""
    
    context_file = Path("examples/sample.ctx.md")
    context_file.parent.mkdir(exist_ok=True)
    context_file.write_text(context_content)
    
    # Create a sample Go file
    go_content = """package main

import (
    "github.com/gin-gonic/gin"
    "github.com/sirupsen/logrus"
    "os"
    "os/signal"
    "syscall"
    "time"
)

// Main application entry point for the Edge Gateway service
func main() {
    // Initialize logger
    log := logrus.New()
    log.SetLevel(logrus.InfoLevel)
    
    // Load configuration
    config := loadConfig()
    
    // Initialize router with middleware
    router := gin.New()
    router.Use(gin.Recovery())
    router.Use(corsMiddleware())
    router.Use(loggingMiddleware(log))
    
    // Setup routes
    setupRoutes(router)
    
    // Start server
    go func() {
        if err := router.Run(config.Address); err != nil {
            log.Fatal("Failed to start server:", err)
        }
    }()
    
    // Wait for interrupt signal
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit
    
    log.Info("Shutting down server...")
}

func loadConfig() *Config {
    return &Config{
        Address: ":8080",
    }
}

type Config struct {
    Address string
}
"""
    
    go_file = Path("examples/sample.go")
    go_file.write_text(go_content)
    
    # Now add AI-CONTEXT comments
    run_command([
        "ccd", "add-context-comments",
        "--file", "examples/sample.go",
        "--context", "examples/sample.ctx.md"
    ], "Adding AI-CONTEXT comments to sample.go")
    
    # Example 2: Extract AI-CONTEXT comments
    print("\n📤 Example 2: Extracting AI-CONTEXT comments")
    print("This will extract and display the AI-CONTEXT comments we just added.")
    
    run_command([
        "ccd", "extract-context",
        "--file", "examples/sample.go"
    ], "Extracting AI-CONTEXT comments from sample.go")
    
    # Example 3: Validate AI-CONTEXT comments
    print("\n✅ Example 3: Validating AI-CONTEXT comments")
    print("This will validate the format and content of the AI-CONTEXT comments.")
    
    run_command([
        "ccd", "validate-context-comments",
        "--file", "examples/sample.go",
        "--report"
    ], "Validating AI-CONTEXT comments with detailed report")
    
    # Example 4: Check context freshness
    print("\n🕒 Example 4: Checking context freshness")
    print("This will check how fresh the context files are.")
    
    run_command([
        "ccd", "context-freshness",
        "--file", "examples/sample.ctx.md"
    ], "Checking freshness of sample.ctx.md")
    
    # Example 5: Check context health
    print("\n🏥 Example 5: Checking context health")
    print("This will analyze the health of the context file.")
    
    run_command([
        "ccd", "context-health",
        "--file", "examples/sample.ctx.md",
        "--detailed"
    ], "Checking health of sample.ctx.md with detailed information")
    
    # Example 6: Run quality gates
    print("\n🚦 Example 6: Running quality gates")
    print("This will run all quality gates for the project.")
    
    run_command([
        "ccd", "quality-gates",
        "--project", "examples"
    ], "Running quality gates on examples directory")
    
    # Example 7: Detect context drift
    print("\n🔍 Example 7: Detecting context drift")
    print("This will check for any drift between context and source files.")
    
    run_command([
        "ccd", "drift-detection",
        "--project", "examples"
    ], "Detecting context drift in examples directory")
    
    # Example 8: Update engineering log
    print("\n📊 Example 8: Updating engineering log")
    print("This will add a new entry to the engineering log.")
    
    run_command([
        "ccd", "update-engineering-log",
        "--description", "Implemented AI-CONTEXT integration example",
        "--impact", "Low",
        "--severity", "Low",
        "--technical-changes", "Created sample files and demonstrated AI-CONTEXT commands",
        "--resolution", "Successfully demonstrated all AI-CONTEXT functionality",
        "--lessons-learned", "AI-CONTEXT integration provides immediate context access",
        "--follow-up", "Extend example to include more language types"
    ], "Adding entry to engineering log")
    
    # Example 9: Create ADR
    print("\n📋 Example 9: Creating Architecture Decision Record")
    print("This will create a new ADR for AI-CONTEXT integration.")
    
    run_command([
        "ccd", "create-adr",
        "--title", "AI-CONTEXT Comments Integration",
        "--status", "Accepted",
        "--context", "Need for direct context access from source code",
        "--decision", "We will integrate AI-CONTEXT comments in all source files",
        "--consequences", "Improved developer experience and AI tool effectiveness"
    ], "Creating ADR for AI-CONTEXT integration")
    
    # Example 10: Check methodology status
    print("\n📈 Example 10: Checking methodology status")
    print("This will show the status of all methodological files.")
    
    run_command([
        "ccd", "methodology-status",
        "--project-dir", "."
    ], "Checking methodology status of current project")
    
    print("\n🎉 All examples completed!")
    print("\n📚 What we demonstrated:")
    print("• AI-CONTEXT comment management (add, extract, validate)")
    print("• Context quality assessment (freshness, health)")
    print("• Quality gates and drift detection")
    print("• Methodology loop integration (engineering log, ADRs)")
    print("• Project status monitoring")
    
    print("\n🧹 Cleaning up example files...")
    try:
        context_file.unlink()
        go_file.unlink()
        print("✅ Cleanup completed")
    except Exception as e:
        print(f"⚠️  Cleanup warning: {e}")

if __name__ == "__main__":
    main()
