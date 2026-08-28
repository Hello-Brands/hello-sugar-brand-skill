// React + Tailwind example using the tailwind-preset.js color/spacing scales.
// Assumes the preset is wired in tailwind.config.js:
//   module.exports = { presets: [require('./tokens/tailwind-preset.js')], content: [...] }
// and assets/fonts/fonts.css is imported once at the app root.

export default function StatCard({ label, value, hint, tone = "primary" }) {
  const toneRing = {
    primary: "ring-hs-primary/20 text-hs-primary",
    accent: "ring-hs-accent/20 text-hs-accent",
    success: "ring-hs-success/20 text-hs-success",
  }[tone];

  return (
    <div className="bg-hs-surface border border-hs-border rounded-lg shadow-md p-6 max-w-xs">
      <span
        className={`inline-block rounded-pill bg-hs-primary-soft px-3 py-0.5 text-xs font-semibold text-hs-deep`}
      >
        {label}
      </span>

      <div className="mt-3 flex items-baseline gap-2">
        <span className="font-sans text-4xl font-bold text-hs-text">{value}</span>
        {hint && <span className="text-sm text-hs-text-muted">{hint}</span>}
      </div>

      <button
        className="mt-5 rounded-pill bg-hs-primary px-5 py-2 font-semibold text-hs-on-primary
                   transition-colors hover:bg-hs-primary-strong
                   focus:outline-none focus:ring-2 focus:ring-hs-focus focus:ring-offset-2"
      >
        View details
      </button>

      <p className={`mt-4 text-sm ${toneRing}`}>Brand-consistent across any tool.</p>
    </div>
  );
}
