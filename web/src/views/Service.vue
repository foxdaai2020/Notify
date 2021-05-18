<template>
  <div>
    <title-bar serviceListFilter="true">Service List</title-bar>
    <title-bar issueTackerFilter="true">Issue Tracker</title-bar>
    <title-bar messageListFilter="true">Message List</title-bar>
  </div>
</template>
<script>
import TitleBar from '../components/TitleBar';

export default {
    components: {
        'title-bar': TitleBar
    }
}
</script>
