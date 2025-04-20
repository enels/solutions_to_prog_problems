const books = [
  {
    title: 'Algorithms',
    author: ['Robert Sedgewick', 'Kevin Wayne'],
    publisher: 'Addison-Wesley Professional',
    publicationDate: '2011-03-24',
    edition: 4,
    keywords: ['computer science', 'programming', 'algorithms', 'data structures', 'java', 'math', 'software', 'engineering'],
    pages: 976,
    format: 'hardcover',
    ISBN: '9780321573513',
    language: 'English',
    programmingLanguage: 'Java',
    onlineContent: true,
    thirdParty: {
      goodreads: {
        rating: 4.41,
        ratingsCount: 1733,
        reviewsCount: 63,
        fiveStarRatingCount: 976,
        oneStarRatingCount: 13
      }
    },
    highlighted: true
  },
  {
    title: 'Structure and Interpretation of Computer Programs',
    author: ['Harold Abelson', 'Gerald Jay Sussman', 'Julie Sussman (Contributor)'],
    publisher: 'The MIT Press',
    publicationDate: '2022-04-12',
    edition: 2,
    keywords: ['computer science', 'programming', 'javascript', 'software', 'engineering'],
    pages: 640,
    format: 'paperback',
    ISBN: '9780262543231',
    language: 'English',
    programmingLanguage: 'JavaScript',
    onlineContent: false,
    thirdParty: {
      goodreads: {
        rating: 4.36,
        ratingsCount: 14,
        reviewsCount: 3,
        fiveStarRatingCount: 8,
        oneStarRatingCount: 0
      }
    },
    highlighted: true
  },
  {
    title: 'Computer Systems: A Programmer\'s Perspective',
    author: ['Randal E. Bryant', 'David Richard O\'Hallaron'],
    publisher: 'Prentice Hall',
    publicationDate: '2002-01-01',
    edition: 1,
    keywords: ['computer science', 'computer systems', 'programming', 'software', 'C', 'engineering'],
    pages: 978,
    format: 'hardcover',
    ISBN: '9780130340740',
    language: 'English',
    programmingLanguage: 'C',
    onlineContent: false,
    thirdParty: {
      goodreads: {
        rating: 4.44,
        ratingsCount: 1010,
        reviewsCount: 57,
        fiveStarRatingCount: 638,
        oneStarRatingCount: 16
      }
    },
    highlighted: true
  },
  {
    title: 'Operating System Concepts',
    author: ['Abraham Silberschatz', 'Peter B. Galvin', 'Greg Gagne'],
    publisher: 'John Wiley & Sons',
    publicationDate: '2004-12-14',
    edition: 10,
    keywords: ['computer science', 'operating systems', 'programming', 'software', 'C', 'Java', 'engineering'],
    pages: 921,
    format: 'hardcover',
    ISBN: '9780471694663',
    language: 'English',
    programmingLanguage: 'C, Java',
    onlineContent: false,
    thirdParty: {
      goodreads: {
        rating: 3.9,
        ratingsCount: 2131,
        reviewsCount: 114,
        fiveStarRatingCount: 728,
        oneStarRatingCount: 65
      }
    }
  },
  {
    title: 'Engineering Mathematics',
    author: ['K.A. Stroud', 'Dexter J. Booth'],
    publisher: 'Palgrave',
    publicationDate: '2007-01-01',
    edition: 14,
    keywords: ['mathematics', 'engineering'],
    pages: 1288,
    format: 'paperback',
    ISBN: '9781403942463',
    language: 'English',
    programmingLanguage: null,
    onlineContent: true,
    thirdParty: {
      goodreads: {
        rating: 4.35,
        ratingsCount: 370,
        reviewsCount: 18,
        fiveStarRatingCount: 211,
        oneStarRatingCount: 6
      }
    },
    highlighted: true
  },
  {
    title: 'The Personal MBA: Master the Art of Business',
    author: 'Josh Kaufman',
    publisher: 'Portfolio',
    publicationDate: '2010-12-30',
    keywords: ['business'],
    pages: 416,
    format: 'hardcover',
    ISBN: '9781591843528',
    language: 'English',
    thirdParty: {
      goodreads: {
        rating: 4.11,
        ratingsCount: 40119,
        reviewsCount: 1351,
        fiveStarRatingCount: 18033,
        oneStarRatingCount: 1090
      }
    }
  },
  {
    title: 'Crafting Interpreters',
    author: 'Robert Nystrom',
    publisher: 'Genever Benning',
    publicationDate: '2021-07-28',
    keywords: ['computer science', 'compilers', 'engineering', 'interpreters', 'software', 'engineering'],
    pages: 865,
    format: 'paperback',
    ISBN: '9780990582939',
    language: 'English',
    thirdParty: {
      goodreads: {
        rating: 4.7,
        ratingsCount: 253,
        reviewsCount: 23,
        fiveStarRatingCount: 193,
        oneStarRatingCount: 0
      }
    }
  },
  {
    title: 'Deep Work: Rules for Focused Success in a Distracted World',
    author: 'Cal Newport',
    publisher: 'Grand Central Publishing',
    publicationDate: '2016-01-05',
    edition: 1,
    keywords: ['work', 'focus', 'personal development', 'business'],
    pages: 296,
    format: 'hardcover',
    ISBN: '9781455586691',
    language: 'English',
    thirdParty: {
      goodreads: {
        rating: 4.19,
        ratingsCount: 144584,
        reviewsCount: 11598,
        fiveStarRatingCount: 63405,
        oneStarRatingCount: 1808
      }
    },
    highlighted: true
  }
];

// Destructuring arrays
// 1.1
let [firstBook, secondBook] = books;

// 1.2
let [thirdBook] = books.slice(2);

// 1.3
//const ratings = [['rating', 4.19], ['ratingsCount', 144584]];
//let [[,rating], [,ratingsCount]] = ratings;

// 1.4
const ratingStars = [63405, 1808];
const [fiveStarRatings, oneStarRatings, threeStarRatings] = [63405, 1808, 0];

// Destructuring Objects
// 2.1
const [title, author, ISBN] = [books[0].title, books[0].author, books[0].ISBN];
// const {title, author, ISBN} = books[0];

// 2.2
const tags = books[0].keywords;
//const {keywords: tags} = books[0];

// 2.3
const {language: language, programmingLanguage: programmingLanguage = 'unknown'}  = books[6];

// 2.4
let bookTitle = 'unknown';
let bookAuthor = 'unknown';

//({title: bookTitle, author: bookAuthor} = books[0]);

// 2.5
// const {thirdParty: {goodreads: {ratings: bookRating}}} = books[0];


// // 2.6
// function printBookInfo({title: title, author: author, publicationDate: year='year unknown'}) {
	
// 	console.log(`${title} by ${author}, ${year.split("-")[0]}`);
// }

// printBookInfo(books[0]);
// printBookInfo({ title: 'Algorithms', author: 'Robert Sedgewick' });

// The Spread Operator
// 3.1
const bookAuthors = [...books[0].author];

// 3.2
/*function spellWord(word) {

	let wordArr = [...word];
	let s = "";

	for (let i = 0; i < wordArr.length; i++)
		s += wordArr[i] + " ";

	console.log(s.trim());
	
}
*/

// function spellWord(word) {
// 	console.log(...word);
// }


// // Rest Pattern and Parameters
// // 4.1
// const [mainKeyword, ...rest] = books[0].keywords;

// // 4.2
// const {publisher: bookPublisher, ...restOfTheBook} = books[1];

// // 4.3
// function printBookAuthorsCount(title, ...authors) {
// 	console.log(`The book ${title} has ${authors.length} authors`);
// }

// Short Circuiting
// 5.1
/*const hasExamplesInJava = function(bookObj) {
	
	if (bookObj.programmingLanguage == "Java")
		return true;
	else
		return "no string";
};

console.log(hasExamplesInJava(books[0]));
// using short circuiting
const hasExamplesInJava = function(bookObj){
	
	return bookObj.programmingLanguage === 'Java' || 'no data available';
};
*/
// 5.2

/*for (let i = 0; i < books.length; i++) {
  books[i].onlineContent && console.log(`"${books[i].title}" provides online content`);
}*/

// for (let i = 0; i < books.length; i++) {
//   !books[i].onlineContent && console.log(`"${books[i].title}" provides no data about its online contents`);
// }

// using the Nullish Coalescing Opeartor
// for (let i = 0; i < books.length; i++) {
//   books[i].onlineContent ?? console.log(`${books[i].title} provides no data about its online content`);

// }

// // 7.1
// for (let i = 0; i < books.length; i++) {
//   books[i].edition ||= 1;
// }

// 7.2

// for (let i = 0; i < books.length; i++) {
//   books[i].highlighted &&= !(books[i].thirdParty.goodreads.rating < 4.2)
//   console.log(books[i].highlighted);

// }

// for-of-loop
// 8.1
// let pagesSum = 0;
// for (const book of books) {
//   pagesSum += book.pages;
// }


// // 8.2
// let allAuthors = [];

// for (const book of books) {
//   if (Array.isArray(book.author)) {
//     for (const theAuthor of book.author) {
//       allAuthors.push(theAuthor);
//     }
//   }
//   else {
//     allAuthors.push(book.author);
//   }
// }

// let authorEntries = allAuthors.entries();

// for (const author of authorEntries) {
//   console.log(`${author[0] + 1}. ${author[1]}`);
// }

// for (const {index, author} of allAuthors.entries()) {
//   console.log(`${index + 1}. ${author}`);
// }

// Ehnanced Object Literals
// 9.1
const bookData = [
  ['title', 'Computer Networking: A Top-Down Approach'],
  ['author', ['James F. Kurose', 'Keith W. Ross']],
  ['publisher', 'Addison Wesley'],
];

// Do the rest
const newBook = {
  [bookData[0][0]]: bookData[0][1],
  [bookData[1][0]]: bookData[1][1],
  [bookData[2][0]]: bookData[2][1]
};

// 9.2
const pages = 880;

const newBook2 = {
  title: 'The C Programming Language',
  author: ['Brian W. Kernighan', 'Dennis M. Ritchie'],
  pages
};

// Obtional Chaining
// function getFirstKeyword(book) {
//    return book.keywords?.[0];
// }

// Looping Objects: Object keys, Values and Entries
// 11.1

// const entries = [[]];

// for (const key of Object.keys(books[0].thirdParty.goodreads)) {
//     entries.push(key);
// }

// for (const [index, value] of Object.values(books[0].thirdParty.goodreads).entries()) {
//   entries[index].push(value);
// }


// 11.3
const entries2 = Object.entries(books[0].thirdParty.goodreads);

// 11.4


// Sets
const allKeywords = [];
const setOfKeywords = new Set();

for (const book of books) {
  book.keywords.forEach((x) => setOfKeywords.add(x));
}

//Jonas
for (const book of books) {
  allKeywords.push(...book.keywords);
}

const uniqueKeywords = new Set(allKeywords);
//setOfKeywords.forEach((x) => allKeywords.push(x));

//allKeywords.push(...setOfKeywords);

// uniqueKeywords.add("coding");
// uniqueKeywords.add("science")

// uniqueKeywords.delete("business");

// const uniqueKeywordsArr = Array.from(uniqueKeywords);

// uniqueKeywords.clear();
// console.log(uniqueKeywords);

// Maps: Fundamentals
// const newBook3 = [['title', 'Clean Code'], ['author', 'Robert C. Martin']];
// const bookMap = new Map();

// newBook3.forEach((book) => bookMap.set(book[0], book[1]));

// console.log(bookMap);

// // 13.3
// bookMap.forEach((values) => console.log(`${values}`));

// //bookMap.forEach((x) => console.log(x));
// console.log(`"${bookMap.get('title')}" by ${bookMap.get('author')}`);

// console.log(bookMap.size);

// if (bookMap.has("author")) {
//   console.log("The author of the book is known");
// }

// Map: Iteration
// 14.1
//const firstBookMap = new Map(Object.entries(books[0]));

// 14.2
// for (const [key, value] of firstBookMap) {
//   if (typeof value === "number") {
//     console.log(key);
//   }
// }

// Wroking with strings

// 15.1
// console.log(books[0].ISBN[6], books[0].ISBN[4], books[0].ISBN[9]);

// console.log(books[0].ISBN['6'], books[0].ISBN['4'], books[0].ISBN['9'], books[0].ISBN[8]);
// // 15.2
// const quote = 'A computer once beat me at chess, but it was no match for me at kick boxing';

// console.log(quote.indexOf("chess"));

// // 15.3
// const word = "boxing";
// console.log(quote.slice(quote.indexOf(word), quote.indexOf(word) + word.length));

// // 15.4
// const isContributor = function(authorName) {
//   console.log(authorName.match(/\(Contributor\)/g) ? true : false);
// }

// // Working with strings
// // 16.1
// const normalizeAuthorName = function(authorName) {
//   //console.log(authorName.split(" ")[0][0].toUpperCase(), authorName.split(" ")[1][0].toUpperCase());

//   let firstName = authorName.split(" ")[0];
//   let lastName = authorName.split(" ")[1];

//   firstName = firstName.toLowerCase().slice(0, 1).toUpperCase() + firstName.toLowerCase().slice(1);
//   lastName = lastName.toLowerCase().slice(0, 1).toUpperCase() + lastName.toLowerCase().slice(1);

//   console.log(firstName, lastName);
// };

// // 16. 2
// const newBookTitle = books[1].title.replace("Programs", "Softwares");

// 16.3
// const logBookTheme = function (bookTitle) {

//   if (bookTitle.startsWith("Computer")) {
//     console.log("This book is about computers");
//   }
//   else if (bookTitle.includes("Algorithms", "Structures")) {
//     console.log("This book is about algorithms and data structures");
//   }
//   else if (bookTitle.match(/[^(operating)] & ((system) | (System) | (systems) | (Systems))$/g)) {
//     console.log("This book is about some systems, but definitely not about operating systems")
//   }

// };

// function logBookTheme(title) {
  // title = title.toLowerCase();
// 
  // if (title.startsWith('computer')) {
    // console.log('This book is about computers');
  // } else if (title.includes('algorithms') && title.includes('structures')) {
    // console.log('This book is about algorithms and data structures');
  // } else if ((title.endsWith('system') || title.endsWith('systems')) && !title.includes('operating')) {
    // console.log('This book is about some systems, but definitely not about operating systems');
  // }
// }
// 
// for (const book of books) {
  // logBookTheme(book.title);
  // console.log(book.title);
// }

// Working with strings
// 17.1
// function logBookCategories (categories) {

//   const catArr = categories.split(";");

//   for (cat of catArr) {
//     console.log(cat);
//   }
// }

// const bookCategories = 'science;computing;computer science;algorithms;business;operating systems;networking;electronics';
// logBookCategories(bookCategories);

// 17.2
const getKeywordsAsString = function (books) {

    let keywordStr = "";

    for (const book of books) {

      // to remove duplicates
      const keywordSet = new Set(book.keywords);

      // convert the set of keywords to an array
      const keywordArr = [];
      keywordSet.forEach((word) => keywordArr.push(word));

      keywordStr += keywordArr.join(";");
    }
    
    return keywordStr;
};

console.log(getKeywordsAsString(books));