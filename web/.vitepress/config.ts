import { defineConfig } from "vitepress";
import tasks from "./sidebar";

export default defineConfig({
  title: 'COMPROG',
  description: '',
  themeConfig: {
    sidebar: [
      {
        collapsible: true,
        text: "grader solutions",
        items: tasks,
      },
    ],
  },
});
