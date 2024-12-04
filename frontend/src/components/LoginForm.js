import React from 'react';

const LoginForm = () => {
  return (
    <div className="form-container">
      <form className="login-form" action="/api/login" method="POST">
        <p className="login-text">Login</p>
        <input
          type="text"
          name="username"
          className="login-input"
          placeholder="Username"
          required
        />
        <input
          type="password"
          name="password"
          className="login-input"
          placeholder="Password"
          required
        />
        <input type="submit" value="Login" className="login-submit" />
      </form>
      <div className="login-links">
        <a href="#" className="login-signup" onClick={() => window.flipTo(1)}>
          アカウントを新しく作成
        </a>
        <a href="#" className="login-forgot-pass">
          パスワードを忘れましたか？
        </a>
      </div>
    </div>
  );
};

export default LoginForm;

