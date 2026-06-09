import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,

  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),

  // 这里添加自定义 rules（覆盖 react-hooks/set-state-in-effect）
  {
    rules: {
      "react-hooks/set-state-in-effect": "off",  // 完全关闭（推荐大多数 next-themes 项目）
      // 或 "warn" 如果你想保留警告但不阻塞开发
      // "react-hooks/set-state-in-effect": "warn",
      'react-hooks/incompatible-library': 'warn',
    },
  },
]);

export default eslintConfig;