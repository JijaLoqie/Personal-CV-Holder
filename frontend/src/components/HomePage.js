import React, { useState } from "react";

export default HomePage = () => {
  const [nickname, setNickname] = useState("JijaLoqie");
  const [cvs, setCvs] = useState([
    { title: "gamedev", type: "pdf", content: "content" },
    { title: "backend", type: "latex", content: "conteeent" },
    { title: "fullstack", type: "html", content: "conteeeeeent" },
  ]);

  return (
    <div>
      <h1>{nickname}</h1>
      <div>
        <ul>
          {cvs.map((cv) => (
            <li>
              {cv.title} ({cv.type}): {cv.content}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};
