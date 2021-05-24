<template>
  <div>
    <!-- =========== Channel List =========== -->
    <title-bar>Channel Information</title-bar>
    <div class="d-flex align-center ma-2">
      <v-btn outlined color="Genoa" small @click="openAddChannelModal = true">
        <v-icon left>
          mdi-plus-circle-outline
        </v-icon>
        Channel</v-btn
      >
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        label="Search"
        single-line
        hide-details
        outlined
        style="max-width:150px"
      ></v-text-field>
    </div>
    <v-data-table
      :headers="channelHeaders"
      :items="channelData"
      :search="search"
    >
      <template v-slot:item.edit>
        <v-icon small @click="openEditChannelModal = true">
          mdi-square-edit-outline
        </v-icon>
      </template>
      <template v-slot:item.leave="{ item }">
        <v-icon small @click="leaveChannel(item.it)">
          mdi-square-edit-outline
        </v-icon>
      </template>
      <template v-slot:item.delete="{ item }">
        <v-icon small @click="deleteChannel(item.id)">
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>

    <!-- =========== Member List =========== -->
    <title-bar>Member List</title-bar>
    <div class="d-flex align-center ma-2">
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        label="Search"
        single-line
        hide-details
        outlined
        style="max-width:150px"
      ></v-text-field>
    </div>
    <v-data-table
      :headers="memberHeaders"
      :items="memberData"
      :search="search"
    ></v-data-table>

    <add-channel-modal
      :openModal="openAddChannelModal"
      @closeModal="openAddChannelModal = false"
    ></add-channel-modal>
    <edit-channel-modal
      :openModal="openEditChannelModal"
      @closeModal="openEditChannelModal = false"
    ></edit-channel-modal>

    <!-- =========== Delete Channel =========== -->
    <title-alert-dialog
      :openDialog="openDeleteDialog"
      @closeDialog="openDeleteDialog = false"
    >
      <template slot="title-icon">mdi-alert</template>
      <template slot="title-text">Delete</template>
      <template slot="content"
        >Are you sure to delete {{ deleteChannelId }} ?</template
      >
      <template slot="action">
        <v-btn
          depressed
          color="DarkGray White--text"
          @click="openDeleteDialog = false"
          >取消</v-btn
        >
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="
            openDeleteDialog = false;
            openConfirmDeleteDialog = true;
          "
          >確定</v-btn
        >
      </template>
    </title-alert-dialog>
    <alert-dialog
      :openDialog="openConfirmDeleteDialog"
      @closeDialog="openConfirmDeleteDialog = false"
    >
      <template slot="content"
        >The channel you want to delete is in service.</template
      >
      <template slot="action">
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="openConfirmDeleteDialog = false"
          >確定</v-btn
        >
      </template>
    </alert-dialog>

    <!-- =========== Leave Channel =========== -->
    <title-alert-dialog
      :openDialog="openLeaveDialog"
      @closeDialog="openLeaveDialog = false"
    >
      <template slot="title-icon">mdi-alert</template>
      <template slot="title-text">Leave</template>
      <template slot="content"
        >Are you sure to leave {{ leaveChannelId }} ?</template
      >
      <template slot="action">
        <v-btn
          depressed
          color="DarkGray White--text"
          @click="openLeaveDialog = false"
          >取消</v-btn
        >
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="
            openLeaveDialog = false;
            openConfirmLeaveDialog = true;
          "
          >確定</v-btn
        >
      </template>
    </title-alert-dialog>
    <alert-dialog
      :openDialog="openConfirmLeaveDialog"
      @closeDialog="openConfirmLeaveDialog = false"
    >
      <template slot="content"
        >You are the ONLY default member of channel.</template
      >
      <template slot="action">
        <v-btn
          depressed
          color="FountainBlue White--text"
          @click="openConfirmLeaveDialog = false"
          >確定</v-btn
        >
      </template>
    </alert-dialog>
    
  </div>
</template>
<script>
  import TitleBar from "../components/TitleBar";
  import AddChannelModal from "../components/modals/AddChannel";
  import EditChannelModal from "../components/modals/EditChannel";
  import AlertDialog from "../components/dialogs/AlertDialog";
  import TitleAlertDialog from "../components/dialogs/TitleAlertDialog";

  export default {
    data: () => {
      return {
        openAddChannelModal: false,
        openEditChannelModal: false,
        openDeleteDialog: false,
        openConfirmDeleteDialog: false,
        openLeaveDialog: false,
        openConfirmLeaveDialog: false,
        deleteChannelId: null,
        leaveChannelId: null,
        search: "",
        channelHeaders: [
          {
            text: "Ch. ID",
            align: "start",
            value: "id",
          },
          { text: "Ch. Name", filterable: false, value: "channelName" },
          { text: "Ch. Token", value: "token" },
          { text: "Desc.", value: "desc" },
          { text: "Default Member", value: "booleanMember" },
          { text: "#Default Member", value: "defaultMember" },
          { text: "#Member", value: "member" },
          { text: "Edit", value: "edit" },
          { text: "Delete", value: "delete" },
          { text: "Leave", value: "leave" },
        ],
        channelData: [
          {
            id: "1",
            channelName: "channelName1",
            token: "token1",
            desc: "desc1",
            booleanMember: "N",
            defaultMember: "defaultMember2",
            member: "member1",
          },
        ],
        memberHeaders: [
          { text: "User Name", value: "userName" },
          { text: "Nickname", value: "nickname" },
          { text: "Default Member", value: "defaultMember" },
          { text: "Org", value: "org" },
        ],
        memberData: [
          {
            userName: "userName1",
            nickname: "nickname1",
            defaultMember: "defaultMember1",
            org: "org1",
          },
        ],
      };
    },
    methods: {
      deleteChannel(id) {
        this.deleteChannelId = id;
        this.openDeleteDialog = true;
      },
      leaveChannel(id) {
        this.leaveChannelId = id;
        this.openLeaveDialog = true;
      },
    },
    components: {
      "title-bar": TitleBar,
      "add-channel-modal": AddChannelModal,
      "edit-channel-modal": EditChannelModal,
      "title-alert-dialog": TitleAlertDialog,
      "alert-dialog": AlertDialog,
    },
  };
</script>
<style lang="scss">
  .v-text-field.v-text-field--outlined {
    .v-label {
      top: unset;
    }

    background: var(--v-White-base);
    .v-input__control .v-input__slot {
      min-height: 20px;
    }
  }
</style>
