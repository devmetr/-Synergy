import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        paper: "var(--paper)",
        "paper-2": "var(--paper-2)",
        ink: "var(--ink)",
        "ink-2": "var(--ink-2)",
        muted: "var(--muted)",
        "muted-2": "var(--muted-2)",
        hairline: "var(--hairline)",
        "hairline-strong": "var(--hairline-strong)",
        accent: "var(--accent)",
        "accent-deep": "var(--accent-deep)",
        "accent-soft": "var(--accent-soft)",
        dark: "var(--dark)",
        "dark-2": "var(--dark-2)",
        "on-dark": "var(--on-dark)",
        "on-dark-muted": "var(--on-dark-muted)",
        "on-dark-hairline": "var(--on-dark-hairline)",
      },
      fontFamily: {
        sans: ["var(--font-sans)", "system-ui", "sans-serif"],
        body: ["var(--font-body)", "system-ui", "sans-serif"],
        serif: ["var(--font-serif)", "Georgia", "serif"],
        mono: ["var(--font-mono)", "ui-monospace", "monospace"],
      },
      borderRadius: {
        DEFAULT: "var(--radius)",
        sm: "calc(var(--radius) - 2px)",
        md: "var(--radius)",
        lg: "calc(var(--radius) + 4px)",
      },
      maxWidth: {
        container: "1200px",
      },
      keyframes: {
        scroll: {
          "0%": { transform: "translateX(0)" },
          "100%": { transform: "translateX(-50%)" },
        },
        "fade-in": {
          "0%": { opacity: "0", transform: "translateY(8px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
      },
      animation: {
        scroll: "scroll 40s linear infinite",
        "fade-in": "fade-in 0.4s ease-out forwards",
      },
    },
  },
  plugins: [],
};

export default config;
