import fs from "node:fs/promises";
import type { DefaultTheme } from "vitepress";

const sidebarItems: DefaultTheme.SidebarItem[] = [];

const createMd = async (file: string) => {
  const comp = file.split(".");
  const fileType = comp[comp.length - 1];

  fs.writeFile(
    `web/tasks/${file}.md`,
    `
# Task: ${file}

\`\`\` ${fileType == "hs" ? "haskell" : fileType}
${(await fs.readFile(`Tasks/${file}`)).toString().trim()}
\`\`\`
    `,
    {
      flag: "w",
    }
  );

  sidebarItems.push({
    text: file,
    link: `/tasks/${file}`,
  });
};

const main = async () => {
  const files = await fs.readdir("Tasks");

  for (const file of files) {
    await createMd(file);
  }

  await fs.writeFile(
    "web/.vitepress/sidebar.ts",
    `
      export default ${JSON.stringify(sidebarItems)};
      `
  );
}

main();
