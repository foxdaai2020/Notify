<template>
  <error-frame>
    <template v-slot:title>
      500 Error
    </template>
    <template v-slot:content>
      Internal Server Error
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