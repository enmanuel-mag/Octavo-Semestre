const funcArray = (CB) => {
  return ['test', 2, { "test": 78 }]
}

const funcobj = () => {
  return { "test": 78 }
}

const [ string, others ] = funcArray();

console.log(string, others)

const { test } = funcobj();

console.log(test)