
const fetchPage = async (url) => {
    let headers = new Headers()
    headers.append("X-Requested-With", "XMLHttpRequest")
    return fetch(url, { headers })
  }
  
  const appendElements = async (scrollElement, counter) => {
    let url = `?page=${counter + 1}`
  
    let req = await fetchPage(url);
  
    if (req.ok) {
      let body = await req.text();
      scrollElement.innerHTML += body;
    } else {
      end = true;
    }
  }
  
  
  const attachInfiniteScroll = (sentinel, scrollElement) => {
    let counter = 1;
    let end = false;
  
    let observer = new IntersectionObserver(async (entries) => {
      let bottomEntry = entries[0];
  
      if (!end && bottomEntry.intersectionRatio > 0) {
        await appendElements(scrollElement, counter);
        counter += 1;
      }
    })
  
  
    observer.observe(sentinel);
  };