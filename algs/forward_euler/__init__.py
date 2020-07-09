import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


def forward_euler_content():
    st.header('Examples')

    example_dd = st.selectbox(
        label="Pick an algorithm:",
        options=['Example 1', 'Example 2'],
    )

    if example_dd == 'Example 1':
        ivp_latex = r'''y'(t)=e^t,\hspace{12pt}y(0)=1'''
        exact_latex = r'''y(t)=e^t'''
        init_val = 1.0
        rhs_fun = np.exp
        sol_fun = np.exp
    else:
        ivp_latex = r'''y'(t)=\cos(t),\hspace{12pt}y(0)=0'''
        exact_latex = r'''y(t)=\sin(t)'''
        init_val = 0.0
        rhs_fun = lambda t: np.cos(2 * t)
        sol_fun = lambda t: 0.5 * np.sin(2 * t)

    st.markdown(r'''Consider the initial value problem''')
    st.latex(ivp_latex)
    st.markdown(r'''with exact solution''')
    st.latex(exact_latex)

    h = st.slider(
        label='Select a step size h',
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        step=0.1,
    )

    t_vals = np.arange(0.0, 4.0 + 1e-12, h)
    exact_sol = sol_fun(t_vals)
    calc_sol = np.zeros(np.shape(t_vals))

    calc_sol[0] = init_val
    for i, _ in enumerate(calc_sol):
        if i == 0:
            continue
        calc_sol[i] = calc_sol[i - 1] + h * rhs_fun(t_vals[i - 1])

    table_data = pd.DataFrame.from_dict({
        'time': t_vals,
        'exact solution': exact_sol,
        'Forward Euler solution': calc_sol,
        'absolute error': np.abs(calc_sol - exact_sol),
    })

    chart_t = np.linspace(0.0, 4.0, 101)
    chart_y = sol_fun(chart_t)

    chart_exact_data = pd.DataFrame.from_dict({
        'series': ['exact'] * len(chart_t),
        'time': chart_t,
        'solution': chart_y,
    })

    chart_euler_data = pd.DataFrame.from_dict({
        'series': ['Forward Euler'] * len(calc_sol),
        'time': t_vals,
        'solution': calc_sol,
    })

    c = alt.Chart(pd.concat([chart_exact_data, chart_euler_data])).mark_line().encode(
        x='time',
        y='solution',
        color='series',
        strokeDash='series',
        tooltip=['time', 'solution']
    )

    st.altair_chart(c, use_container_width=True)
    st.dataframe(table_data)
