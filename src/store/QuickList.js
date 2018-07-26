class QuickList {
  constructor() {
    this.collections = [];
    this.update();
  }

  add(collection) {
    this.collections.push(collection);
    this.update();
  }

  remove(index) {
    this.collections.splice(index, 1);
    this.update();
  }

  clearAll() {
    this.collections = [];
    this.update();
  }

  update() {
    this.len = this.collections.length;
    this.visible = this.len > 0;
  }

  displayStr(collection) {
    return `${collection[0]} ${collection[1]} ${collection[2]}`;
  }
}

export default QuickList;
