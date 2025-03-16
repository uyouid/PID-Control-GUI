import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from control import feedback, tf
from control.matlab import bode, step

from tf_model import tf_1st_order_lag_model, tf_2nd_order_lag_model


def main() -> None:
    st.sidebar.title("Model option")
    model_option = st.sidebar.selectbox("Select model", ["1st order lag model", "2nd order lag model"])
    g = tf_1st_order_lag_model()
    if model_option == "2nd order lag model":
        g = tf_2nd_order_lag_model()

    st.sidebar.title("Gain Control")
    kp = st.sidebar.slider(label="kp", value=0.0, max_value=10.0, min_value=0.0, step=0.1, format="%.1f")
    ki = st.sidebar.slider(label="ki", value=0.0, max_value=10.0, min_value=0.0, step=0.1, format="%.1f")
    kd = st.sidebar.slider(label="kd", value=0.0, max_value=10.0, min_value=0.0, step=0.1, format="%.1f")

    col1, col2 = st.columns(2)
    k = tf([kd, kp, ki], [1, 0])
    sys = feedback(g * k, 1)
    with col1:
        st.header("Step response")
        time = np.linspace(0, 5, 1000)
        y, t = step(sys, time)
        fig1 = plt.figure()
        plt.xlabel("time")
        plt.ylabel("response")
        plt.grid()
        plt.plot(t, y)
        plt.axhline(1, color="k", linestyle="--")
        st.pyplot(fig1)

    with col2:
        st.header("Bode plot")
        gain, phase, w = bode(sys)
        fig2 = plt.figure()
        plt.subplot(2, 1, 1)
        plt.ylabel("Magnitude [dB]")
        plt.grid()
        if gain[0] != 0:
            plt.semilogx(w, 20 * np.log10(gain))

        plt.subplot(2, 1, 2)
        plt.xlabel("Frequency [rad/s]")
        plt.ylabel("Phase [deg]")
        plt.grid()
        plt.semilogx(w, phase * 180 / np.pi)
        st.pyplot(fig2)


if __name__ == "__main__":
    main()
