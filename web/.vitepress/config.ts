import { defineConfig } from "vitepress";
import tasks from "./sidebar";

export default defineConfig({
  lang: "en-US",
  // base: "/2110101-com-prog",
  base: "/",
  title: "COMPROG",
  outDir: "../dist/",
  description: "",

  head: [
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=IBM+Plex+Sans+Thai:r,i,b,bi",
      },
    ],
  ],

  themeConfig: {
    siteTitle: "COMPROG",
    sidebar: [
      {
        collapsible: true,
        text: "grader solutions",
        items: tasks,
      },
    ],
    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/mark48853/2110101-com-prog",
      },
    ],
    footer: {
      message: "Released under the MIT License.",
      copyright: "Copyright © 2022-Sathana Laolugsanalerd",
    },
  },
});
