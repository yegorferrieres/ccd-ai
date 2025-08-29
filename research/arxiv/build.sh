#!/bin/bash

# CCD LaTeX Paper Build Script
# This script compiles the CCD paper for arXiv submission

set -e  # Exit on any error

echo " Building CCD LaTeX Paper..."

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo " Error: pdflatex is not installed"
    echo "Please install a LaTeX distribution (e.g., TeX Live, MiKTeX)"
    exit 1
fi

# Clean previous builds
echo " Cleaning previous builds..."
rm -f *.aux *.log *.out *.toc *.pdf

# First pass - generate auxiliary files
echo " First pass: generating auxiliary files..."
pdflatex -interaction=nonstopmode paper.tex

# Second pass - resolve references
echo " Second pass: resolving references..."
pdflatex -interaction=nonstopmode paper.tex

# Check if PDF was generated
if [ -f "paper.pdf" ]; then
    echo " Success! Paper compiled successfully"
    echo " Output: paper.pdf"
    
    # Show file size
    ls -lh paper.pdf
    
    # Check for warnings in log
    if grep -q "Warning" paper.log; then
        echo "  Warnings found in paper.log - please review"
    fi
    
    # Check for errors in log
    if grep -q "Error" paper.log; then
        echo " Errors found in paper.log - please review"
    fi
else
    echo " Error: PDF generation failed"
    echo "Check paper.log for details"
    exit 1
fi

echo "Build complete!"
echo ""
echo "Next steps:"
echo "1. Review paper.pdf for formatting"
echo "2. Check paper.log for warnings/errors"
echo "3. Submit to arXiv if ready"
echo ""
echo " arXiv submission:"
echo "- paper.pdf is ready for upload"
echo "- Source files can be included as supplementary material"
