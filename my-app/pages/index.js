import { Flex } from "@chakra-ui/react";
import React, { useEffect, useState, useRef } from "react";
import { ForceGraph } from "../components/forcegraph";

export default function Home() {
  const formRef = useRef(null);
  const [selectedFile, setSelectedFile] = useState("");
  const [csvArr, setCsvArr] = useState(null);
  // graph payload (with minimalist structure)

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Selected file - ${formRef.current.files[0].name}`);
    setSelectedFile(formRef.current.files[0]);
  };

  function csvToArray(str, delimiter = ",") {
    // slice from start of text to the first \n index
    // use split to create an array from string by delimiter
    const headers = str.slice(0, str.indexOf("\n")).split(delimiter);

    // slice from \n index + 1 to the end of the text
    // use split to create an array of each csv value row
    const rows = str.slice(str.indexOf("\n") + 1).split("\n");

    // Map the rows
    // split values from each row into an array
    // use headers.reduce to create an object
    // object properties derived from headers:values
    // the object passed as an element of the array
    const arr = rows.map(function (row) {
      const values = row.split(delimiter);
      const el = headers.reduce(function (object, header, index) {
        object[header] = values[index];
        return object;
      }, {});
      return el;
    });

    // return the array
    return arr;
  }

  useEffect(() => {
    // console.log("hit")
    (async () => {
      if (selectedFile) {
        const text = await selectedFile.text();
        const array = csvToArray(text);
        console.log(array);
        setCsvArr(array);
      }
    })();
  }, [selectedFile]);

  return (
    <Flex
      direction="column"
      alignItems="center"
      justifyContent="center"
      minHeight="70vh"
      gap={4}
      mb={8}
      w="full"
    >
      <ForceGraph data={csvArr} />
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          ref={formRef}
          defaultValue={selectedFile}
          // onChange={(e) => setSelectedFile(e.target.files[0])}
        />
        <br />
        <button type="submit">Submit</button>
      </form>
    </Flex>
  );
}
