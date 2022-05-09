from common import Problem
import fire
import re


LATEX_ESCAPES = {
    '&':  r'\&',
    '%':  r'\%', 
    '$':  r'\$', 
    '#':  r'\#', 
    '_':  r'\_', 
    '{':  r'\letteropenbrace{}', 
    '}':  r'\letterclosebrace{}',
    '~':  r'\lettertilde{}', 
    '^':  r'\letterhat{}', 
    '\\': r'\letterbackslash{}',
}

def escape_latex(s):
    if isinstance(s, str):
        # https://stackoverflow.com/questions/16259923/how-can-i-escape-latex-special-characters-inside-django-templates/16264094#16264094
        return "".join([LATEX_ESCAPES.get(char, char) for char in s])
    else:
        return str(s)


def format_listing_var(m):
    id = escape_latex(m.group(1))
    return "{(*\\textbf{\\color{gridvar}" + id + "}*)}"

def value_to_latex(v):
    latex = escape_latex(v)
    if isinstance(v, str):
        latex = f"'{latex}'"
    latex = f"\\texttt{{{latex}}}"

    return latex

def main(problem_name):
    problem = Problem(problem_name)
    text = problem.get_text()
    listing = re.sub(r"\{([_a-z0-9]+)\}", format_listing_var, text)

    grid = problem.grid
    
    table = """\\begin{tabular}{p{0.35\\linewidth} | >{\\raggedright\\arraybackslash}p{0.6\\linewidth}}
    \\toprule
    \\textbf{Variable} & \\textbf{Values} \\\\
    \\midrule\n"""

    for var, values in grid.items():
        clean_var = escape_latex(var)
        clean_values = ', '.join(value_to_latex(v) for v in values)
        table += f"    \\texttt{{{clean_var}}} & {clean_values} \\\\ \n"
    table += "    \\bottomrule\n"
    table += "\\end{tabular}"

    # print(listing)
    # print(table)


    figure = r"""
\begin{figure*}[!htbp]
    \begin{minipage}{.6\textwidth}
	\begin{lstlisting}[language=Python, numbers=none]
    $listing
    \end{lstlisting}
    \end{minipage}
    \begin{minipage}{.3\textwidth}
    $table
    \end{minipage}
	\caption{$caption}
	\label{fig:gcd}
\end{figure*}
""".replace('$listing', listing).replace('$table', table).replace("$caption", escape_latex(problem_name))
    print(figure)


if __name__ == '__main__':
    fire.Fire(main)