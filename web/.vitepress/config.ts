import { defineConfig } from "vitepress";
import tasks from "./sidebar";

export default defineConfig({
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
