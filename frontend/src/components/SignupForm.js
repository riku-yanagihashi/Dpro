import React from 'react';

const SignupForm = () => {
  return (
    <div className="form-container">
      <form className="login-form" action="/api/signup" method="POST">
        <p className="login-text">Signup</p>
        <input
          type="text"
          name="username"
          className="login-input"
          placeholder="Username"
          required
        />
        <input
          type="email"
          name="email"
          className="login-input"
          placeholder="Email"
          required
        />
        <input
          type="password"
          name="password1"
          className="login-input"
          placeholder="Password"
          required
        />
        <input
          type="password"
          name="password2"
          className="login-input"
          placeholder="Confirm Password"
          required
        />
        <input type="submit" value="Sign Up" className="login-submit" />
      </form>
      <div className="login-links">
        <a href="#" className="login-signup" onClick={() => window.flipTo(0)}>
          既にアカウントをお持ちの方はこちら
        </a>
      </div>
    </div>
  );
};

export default SignupForm;

