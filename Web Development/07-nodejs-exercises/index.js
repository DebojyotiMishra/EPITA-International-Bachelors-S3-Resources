const student = {
  name: "Marie",
  age: 20,
  courses: [],
};

student.age = 21;
student.grade = "A";
student.courses.push("Math", "Physics", "Chemistry");

console.log(student);
console.log("Index of Physics:", student.courses.indexOf("Physics"));
console.log("First two courses:", student.courses.slice(0, 2));

// ========== Output on running 'node index.js' =============
// {
//     name: 'Marie',
//     age: 21,
//     courses: [ 'Math', 'Physics', 'Chemistry' ],
//     grade: 'A'
//   }
//   Index of Physics: 1
//   First two courses: [ 'Math', 'Physics' ]
// ==========================================================