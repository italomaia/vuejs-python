VueListModel = Vue.extend
  data:
    results: []
    count: 0
    new_posts: false

  ready: ->
    el = $ this.$el
    src = el.attr 'src'
    $.get(src).done (data) => this.$data = data

    socket.on 'new posts', => Materialize.toast('New Post! Press F5 to update.', 3000)


$ -> $('[vue-list]').each -> new VueListModel el: this
