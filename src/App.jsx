import { createRoot } from "react-dom/client";
import Job from "./Job";
import { useState } from "react";
import SetTitle from "./SetTitle";

const App = () => {
  const JOBS = [
    {
      id: 1,
      jobTitle: "Full Stack Developer",
      company: "Dentsu",
      description: "Working on PR Metrics and Architect.",
    },
    {
      id: 2,
      jobTitle: "T3 Support Engineer",
      company: "UserTesting",
      description:
        "Providing T3 support for UserZoom and UserTesting customers.",
    },
    {
      id: 3,
      jobTitle: "Database Administrator",
      company: "Welcome Break",
      description: "Looked after databases for Welcome Break.",
    },
  ];

  return (
    <div>
      <h1>Aaron Barratt</h1>
      {JOBS.map((job) => (
        <Job
          key={job.id}
          jobTitle={job.jobTitle}
          jobCompany={job.company}
          jobDescription={job.description}
        />
      ))}
      <SetTitle />
    </div>
  );
};

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);
