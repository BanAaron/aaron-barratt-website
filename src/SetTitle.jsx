import { useState } from "react";

const SetTitle = () => {
  const [title, setTitle] = useState("aaronbarratt.dev");
  document.title = title
  return (
    <>
      <label htmlFor="title">
        Title
        <input
          id="title"
          type="text"
          onChange={(e) => setTitle(e.target.value)}
        />
      </label>
    </>
  );
};

export default SetTitle;
