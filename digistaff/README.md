# Digistaff

Премиум-лендинг IT-аутстаффинговой компании Digistaff.

## Стек

- Next.js 15 (App Router) · TypeScript (strict)
- Tailwind CSS 3 с кастомными токенами из `tailwind.config.ts` + `app/globals.css`
- Framer Motion (анимации)
- react-hook-form + zod (форма заявки)
- Шрифты через `next/font/google`: Space Grotesk · Manrope · Cormorant Garamond italic · JetBrains Mono

## Команды

```bash
npm install
npm run dev        # http://localhost:3000
npm run build
npm run lint
npm run typecheck
```

## Переменные окружения

| Переменная | Значения | Назначение |
|---|---|---|
| `NEXT_PUBLIC_HERO_VARIANT` | `A` · `B` · `C` | Вариант первого экрана. По умолчанию `B` (editorial split). |

## Структура

```
app/
  layout.tsx     — шрифты, метаданные, Schema.org
  page.tsx       — сборка лендинга
  globals.css    — токены (CSS-переменные) + base-стили
components/      — секции, hero-варианты, UI-атомы (добавляются при переносе прототипа)
```

## Дизайн-правила

См. бриф. Кратко: оранжевый `#FF5A1F` + ink `#0B0B0B`, паперный фон, italic-акценты Cormorant, минимальный radius `4px`, хайрлайны вместо теней, табличные цифры.
