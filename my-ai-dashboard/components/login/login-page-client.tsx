"use client";

import { FormEvent, useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";

import { getStoredSession } from "@/lib/auth";
import { getErrorMessage } from "@/lib/error";
import { login } from "@/services/auth";
import type { AuthMessage, UserRole } from "@/types/auth";

function getGreetingByHour() {
  const hour = new Date().getHours();

  if (hour < 6) return "Night shift monitoring in progress";
  if (hour < 12) return "Good morning, review store operations";
  if (hour < 18) return "Good afternoon, check lunch and dinner traffic";
  return "Good evening, prepare the daily close summary";
}

const ROLE_OPTIONS: UserRole[] = ["admin", "manager", "operator"];

export default function LoginPageClient() {
  const router = useRouter();
  const [currentRole, setCurrentRole] = useState<UserRole>("admin");
  const [account, setAccount] = useState("");
  const [password, setPassword] = useState("");
  const [remember, setRemember] = useState(true);
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<AuthMessage>(null);

  const greeting = useMemo(() => getGreetingByHour(), []);

  useEffect(() => {
    const session = getStoredSession();
    if (session?.tokens.accessToken) {
      router.replace("/dashboard/overview");
    }
  }, [router]);

  function showMessage(text: string, type: "success" | "error") {
    setMessage({ text, type });
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setMessage(null);

    try {
      await login(account.trim(), password, remember);
      showMessage("Login success. Redirecting...", "success");
      router.replace("/dashboard/overview");
    } catch (error) {
      showMessage(getErrorMessage(error), "error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="page">
      <section className="panel hero">
        <header className="brand">
          <div className="brand-left">
            <div className="brand-badge">RS</div>
            <div>
              <h1 className="brand-title">RestaurantOS</h1>
              <p className="brand-subtitle">Login gateway</p>
            </div>
          </div>
          <div className="brand-status">{greeting}</div>
        </header>

        <div className="hero-main">
          <div className="hero-copy">
            <div className="hero-banner">
              <div>
                <div className="eyebrow">Auth skeleton reconnected</div>
                <h2 className="hero-title">
                  Login, me, refresh, session storage, and route guard are back.
                  <br />
                  Only field mapping stays isolated for you to adjust.
                </h2>
                <p className="hero-desc">
                  The request flow is wired again, while response-field parsing is centralized in
                  `lib/api/auth-mappers.ts` so you only need to adapt one place when final backend
                  fields are confirmed.
                </p>
              </div>

              <div className="hero-stats">
                <div className="hero-stat">
                  <div className="label">Login</div>
                  <div className="value">wired</div>
                  <div className="hint">service plus storage</div>
                </div>
                <div className="hero-stat">
                  <div className="label">Refresh</div>
                  <div className="value">wired</div>
                  <div className="hint">body field may need mapping</div>
                </div>
                <div className="hero-stat">
                  <div className="label">Mapping</div>
                  <div className="value">isolated</div>
                  <div className="hint">edit one mapper file only</div>
                </div>
              </div>
            </div>
          </div>

          <div className="hero-side">
            <div className="mini-card">
              <h3>Where to edit</h3>
              <p>
                If backend fields differ, adjust the request body in `services/auth.ts` and the
                response parsing in `lib/api/auth-mappers.ts`.
              </p>
              <div className="module-grid">
                <div className="module-item">login</div>
                <div className="module-item">me</div>
                <div className="module-item">refresh</div>
                <div className="module-item">guard</div>
                <div className="module-item">storage</div>
                <div className="module-item">logout</div>
              </div>
            </div>

            <div className="mini-card">
              <h3>Current role</h3>
              <p>This role switch is still UI-only unless you decide to send role in the request.</p>
              <ul className="tips-list">
                <li>
                  <span className="dot" />
                  <span>The account and password fields submit to the real login endpoint.</span>
                </li>
                <li>
                  <span className="dot" />
                  <span>Backend messages now pass through directly.</span>
                </li>
                <li>
                  <span className="dot" />
                  <span>401 responses clear stored session automatically.</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <section className="login-wrap">
        <div className="login-card panel-solid">
          <div className="login-head">
            <div>
              <h2 className="login-title">Reconnect login</h2>
              <p className="login-subtitle">Only auth field mapping remains for you to adjust.</p>
            </div>
            <div className="notify-pill">Auth ready</div>
          </div>

          <div className="role-switch">
            {ROLE_OPTIONS.map((role) => (
              <button
                key={role}
                className={`role-btn ${currentRole === role ? "active" : ""}`}
                type="button"
                onClick={() => setCurrentRole(role)}
              >
                {role}
              </button>
            ))}
          </div>

          <form onSubmit={handleSubmit}>
            <div className="field">
              <label htmlFor="account">Account</label>
              <div className="input-wrap">
                <input
                  id="account"
                  className="input"
                  type="text"
                  placeholder="Enter account"
                  autoComplete="username"
                  value={account}
                  onChange={(event) => setAccount(event.target.value)}
                />
              </div>
            </div>

            <div className="field">
              <label htmlFor="password">Password</label>
              <div className="input-wrap">
                <input
                  id="password"
                  className="input password"
                  type={passwordVisible ? "text" : "password"}
                  placeholder="Enter password"
                  autoComplete="current-password"
                  value={password}
                  onChange={(event) => setPassword(event.target.value)}
                />
                <button
                  type="button"
                  className="toggle-password"
                  aria-label="toggle password visibility"
                  onClick={() => setPasswordVisible((prev) => !prev)}
                >
                  {passwordVisible ? "hide" : "show"}
                </button>
              </div>
            </div>

            <div className="form-meta">
              <label className="remember">
                <input
                  type="checkbox"
                  checked={remember}
                  onChange={(event) => setRemember(event.target.checked)}
                />
                <span>Remember me</span>
              </label>

              <button
                className="link-btn"
                type="button"
                onClick={() => showMessage("Forgot-password endpoint is declared but not wired yet.", "success")}
              >
                Forgot password
              </button>
            </div>

            <button className="submit-btn" type="submit" disabled={loading}>
              <span>{loading ? "Processing..." : "Log in"}</span>
              <span>{">"}</span>
            </button>

            <div className={`message ${message ? `show ${message.type}` : ""}`}>{message?.text}</div>
          </form>

          <div className="footer-note">Adjust only the auth mapper file when backend fields are finalized.</div>
        </div>
      </section>
    </div>
  );
}
