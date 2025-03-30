# Iris Analyzer

A Python package for analyzing and visualizing the Iris dataset.

## Installation

1. Clone the repository and install the package locally:

    ```bash
    git clone <your-github-url>
    ```

2. Create a virtual environment and install the package:

    ```bash
    python3 -m venv .venv
    ```

3. Activate the virtual environment:

    | Linux/MacOS                 | Windows                  |
    | --------------------------- | ------------------------ |
    | `source .venv/bin/activate` | `.venv\Scripts\activate` |

4. Install the package:

    ```bash
    pip3 install .
    ```


## Usage

```python
from iris_analyzer import IrisAnalyzer, IrisVisualizer

analyzer = IrisAnalyzer("data/iris.csv")
summary = analyzer.get_summary()
filtered = analyzer.filter_by_species("Iris-setosa")

visualizer = IrisVisualizer(analyzer.data)
visualizer.plot_pairwise()
```

## License

This project is licensed under the MIT License.
