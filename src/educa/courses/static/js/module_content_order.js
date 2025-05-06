let options = {
    method: 'POST',
    mode: 'same-origin'
}

const moduleOrderUrl = "/course/module/order/";

sortable('#modules', {
  forcePlaceholderSize: true,
  placeholderClass: 'placeholder'
})[0].addEventListener('sortupdate', function(e) {

  let modulesOrder = {};
  let modules = document.querySelectorAll('#modules li');
  modules.forEach(function (module, index) {
    modulesOrder[module.dataset.id] = index;
    module.querySelector('.order').innerHTML = index + 1;
    options['body'] = JSON.stringify(modulesOrder);

    fetch(moduleOrderUrl, options)
  });
});

const contentOrderUrl = "/course/content/order/";

sortable('#module-contents', {
  forcePlaceholderSize: true,
  placeholderClass: 'placeholder'
})[0].addEventListener('sortupdate', function(e) {

  let contentOrder = {};
  let contents = document.querySelectorAll('#module-contents div');
  contents.forEach(function (content, index) {
    contentOrder[content.dataset.id] = index;
    options['body'] = JSON.stringify(contentOrder);

    fetch(contentOrderUrl, options)
  });
});