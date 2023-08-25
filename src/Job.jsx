const Job = (props) => {
  return (
    <div className="job">
      <h2>{props.jobTitle}</h2>
      <h2>{props.jobCompany}</h2>
      <p>{props.jobDescription}</p>
    </div>
  );
};

export default Job;
