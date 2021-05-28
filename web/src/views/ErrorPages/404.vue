<template>
  <error-frame>
    <template v-slot:title>
      404 Not Found
    </template>
    <template v-slot:content>
      The URL you requested was not found.
    </template>
  </error-frame>
</template>

<script>
  import ErrorFrame from "@/components/ErrorFrame";

  export default {
    components: {
      "error-frame": ErrorFrame,
    }
  }
</script>