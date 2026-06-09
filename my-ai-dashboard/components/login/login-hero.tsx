import { LoginHeroBanner } from "./login-hero-banner";
import { LoginHeroSide } from "./login-hero-side";

export function LoginHero({ greeting }: { greeting: string }) {
  return (
    <section className="panel hero">
      <header className="brand">
        <div className="brand-left">
          <div className="brand-badge">🍽</div>
          <div>
            <h1 className="brand-title">RestaurantOS</h1>
            <p className="brand-subtitle">智能运营中心 · 登录入口</p>
          </div>
        </div>
        <div className="brand-status">{greeting}</div>
      </header>

      <div className="hero-main">
        <div className="hero-copy">
          <LoginHeroBanner />
        </div>

        <LoginHeroSide />
      </div>
    </section>
  );
}
