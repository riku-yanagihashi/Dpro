import React, { useEffect } from 'react';

const ExampleComponent = () => {
  useEffect(() => {
    fetch('http://localhost:8000/api/example/')
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error('Error:', error));
  }, []);

  return <div>Check the console for API response!</div>;
};

export default ExampleComponent;
