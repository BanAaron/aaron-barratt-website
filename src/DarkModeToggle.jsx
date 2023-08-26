import { useState } from "react";

const DarkModeToggle = () => {
  const [darkMode, setDarkMode] = useState(true);

  function toggle() {
    if (darkMode) {
      setDarkMode(false);
    } else {
      setDarkMode(true);
    }
  }

  return (
    <div>
      <button onClick={toggle}>Dark Mode</button>
      <link
        rel="stylesheet"
        href={darkMode ? "./dark-style.css" : "./light-style"}
      />
    </div>
  );
};

export default DarkModeToggle;
