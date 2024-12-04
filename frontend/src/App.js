import React from 'react';
import HTMLFlipBook from 'react-pageflip';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import './App.css';

const App = () => {
  return (
    <div className="app">
      <HTMLFlipBook
        width={400}
        height={600}
        size="fixed"
        showCover={true}
        className="flipbook"
      >
        <div className="page">
          <LoginForm />
        </div>
        <div className="page">
          <SignupForm />
        </div>
      </HTMLFlipBook>
      <div className="underlay-photo"></div>
      <div className="underlay-black"></div>
    </div>
  );
};

export default App;
