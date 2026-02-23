# AI Agent Instructions for Intro-LLMs

## Project Overview
This is an educational project introducing the Hugging Face Transformers library. It consists of a single Jupyter notebook that explores transformer models and related NLP concepts.

## Project Structure
- `intro_to_transformers_library.ipynb` - Main learning notebook with transformer experiments
- `requirements.txt` - Dependencies (transformers, Pillow, gradio, openai, polars, seaborn, scikit-learn)

## Key Technologies
- **Transformers**: Hugging Face library for state-of-the-art NLP/ML models
- **Gradio**: UI framework for creating demos
- **OpenAI API**: For LLM integration examples
- **Data Tools**: Polars (dataframes), scikit-learn (ML utilities), seaborn/matplotlib (visualization)
- **Image Processing**: Pillow for vision-related tasks

## Working with the Notebook
When modifying or extending `intro_to_transformers_library.ipynb`:

1. **Execution**: Run cells sequentially using notebook tools; dependencies are loaded in first cell
2. **Output**: Expect model outputs, visualizations, and demo interfaces
3. **Installation**: All dependencies are in `requirements.txt` - ensure fresh environment before running
4. **Common Patterns**:
   - Load pre-trained models from Hugging Face Hub (e.g., `transformers.pipeline()`)
   - Chain multiple transformers for task composition
   - Use Gradio for quick interactive demos

## AI Agent Best Practices
- **Before modifying cells**: Run existing cells to understand current state and dependencies
- **Adding content**: Keep explanations concise; this is a learning notebook, not comprehensive documentation
- **Dependencies**: Any new imports must be added to `requirements.txt`
- **Testing**: Validate code snippets work end-to-end before committing
- **Documentation**: Add markdown cells explaining "why" before complex code sections

## Common Development Tasks
```bash
# Install environment
pip install -r requirements.txt

# Run notebook (from terminal or VS Code)
jupyter notebook intro_to_transformers_library.ipynb
```
